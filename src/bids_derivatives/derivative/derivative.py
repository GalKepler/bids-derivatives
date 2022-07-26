from pathlib import Path
from typing import Union

from parse import parse

from bids_derivatives.derivative.messages import (
    PARTICIPANT_COULD_NOT_BE_DETERMINED,
    PARTICIPANT_MISMATCH,
    PARTICIPANT_MISSING,
)
from bids_derivatives.utils.templates import SESSION_TEMPLATE, SUBJECT_TEMPLATE


class SingleSubjectDerivative:
    """
    A SingleDerivative is a class that perform queries on the
    BIDS-App at a single participant level.
    """

    def __init__(
        self,
        base_directory: Union[str, Path],
        participant_label: str = None,
        exists: bool = True,
    ):
        self.participant_label = self.validate_participant_label(
            participant_label
        )
        self.base_directory = self.validate_base_directory(base_directory)
        self.exists = exists

    def get_participant_path(self):
        """
        Get the path to the participant's derivatives directory.
        """
        result = self.base_directory / SUBJECT_TEMPLATE.format(
            subject=self.participant_label
        )
        if not result.exists() and self.exists:
            raise ValueError(
                PARTICIPANT_MISSING.format(
                    participant_label=self.participant_label,
                    base_directory=self.base_directory,
                )
            )
        return result

    def validate_participant_label(self, participant_label: str):
        """
        Validate the participant label.
        """
        if participant_label is not None:
            parser = parse(SUBJECT_TEMPLATE, participant_label)
            if parser:
                participant_label = parser.named.get("subject")
            else:
                pass  # Keep participant label as is.
        return participant_label

    def validate_base_directory(self, base_dir: Union[Path, str]):
        """
        Validate the participant label from either a subject-specific directory
        or a specified label.

        Parameters
        ----------
        base_dir : Path
            The base directory of the BIDS-App.
        participant_label : str, optional
            The participant label, by default None

        Returns
        -------
        Path
            The validated base directory.

        Raises
        ------
        ValueError
            If the base directory is at the single subject's level
            and participant label inferred by it does not match the one
            given as input.
        """
        base_dir = Path(base_dir)
        base_dir_name = base_dir.name
        root_directory_at_participant = (
            self.validate_base_dir_participant_mismatch(base_dir_name)
        )
        return base_dir.parent if root_directory_at_participant else base_dir

    def validate_base_dir_participant_mismatch(
        self, base_dir_name: str
    ) -> bool:
        """
        Validate the if base directory is at the single subject's level,
        the participant label inferred by it matches the one given as input.

        Parameters
        ----------
        base_dir_name : str
            The base directory name.

        Returns
        -------
        bool
            True if the base directory is at the single subject's level,

        Raises
        ------
        ValueError
            _description_
        ValueError
            _description_
        """
        parser = parse(SUBJECT_TEMPLATE, base_dir_name)
        if self.participant_label is not None:
            if parser:
                participant_label = parser.named.get("subject")
                if self.participant_label != participant_label:
                    raise ValueError(
                        PARTICIPANT_MISMATCH.format(
                            participant_label=self.participant_label,
                            base_dir_name=participant_label,
                        )
                    )
        else:
            if parser:
                self.participant_label = parser.named.get("subject")
            else:
                raise ValueError(PARTICIPANT_COULD_NOT_BE_DETERMINED)
        return parser

    def get_available_sessions(self):
        """
        Query the participant's derivatives directory for available sessions.
        """
        sessions = []
        for session in self.path.iterdir():
            parser = parse(SESSION_TEMPLATE, session.name)
            if parser:
                sessions.append(parser.named.get("session"))
        return list(set(sessions))

    @property
    def path(self):
        """
        Get the path to the participant's derivatives directory.
        """
        return self.get_participant_path()

    @property
    def analysis_title(self) -> str:
        """
        Get the analysis title.
        """
        return self.base_directory.name

    @property
    def sessions(self):
        """
        Get the available sessions.
        """
        return self.get_available_sessions()
