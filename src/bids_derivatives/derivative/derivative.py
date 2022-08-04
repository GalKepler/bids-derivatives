from pathlib import Path
from typing import Union

from bids.layout.models import Config
from bids.utils import listify
from parse import parse

from bids_derivatives.bids_apps.outputs.outputs import validate_outputs
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

    #: Default configurations
    DEAFULT_CONFIGURATIONS = ["bids", "derivatives"]

    def __init__(
        self,
        base_directory: Union[str, Path],
        participant_label: str = None,
        exists: bool = True,
        layout_configuration: Union[str, dict] = None,
        output_configuration: Union[dict, list] = None,
        required_keys: list = ["entities"],
    ):
        """
        Instansiate a `SingleSubjectDerivative` object.

        Parameters
        ----------
        base_directory : Union[str, Path]
            Base directory for the BIDS-app's outputs
        participant_label : str, optional
            Participant's label (either sub-xxx or its identifier),
            by default None
        exists : bool, optional
            Whether the participant exists (mainly used for debugging),
            by default True
        output_configuration : Union[dict, list], optional
            A dictionary describing BIDS-app outputs, by default None
        """
        self.participant_label = self.validate_participant_label(
            participant_label
        )
        self.base_directory = self.validate_base_directory(base_directory)
        self.exists = exists
        self.layout_configurations = self.get_configurations(
            layout_configuration
        )
        self.output_configuration = validate_outputs(
            output_configuration, required_keys=required_keys
        )

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

    def locate_output(self, entities: dict) -> Path:
        """
        Locate the output path for the given entities.

        Parameters
        ----------
        entities : dict
            A dictionary containing the entities to locate the output for.

        Returns
        -------
        Path
            The output path.

        Raises
        ------
        ValueError
            If the output path cannot be determined.
        """
        output_path = self.get_output_path(entities)
        if not output_path.exists():
            raise ValueError(
                "Output path does not exist: {}".format(output_path)
            )
        return output_path

    def get_configurations(self, layout_configuration: Union[str, dict]):
        """
        Get the layout and output configurations.
        """
        return [
            Config.load(config)
            for config in self.DEAFULT_CONFIGURATIONS
            + listify(layout_configuration)
        ]

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

    @property
    def configurations(self):
        return {c.name.lower(): c for c in self.layout_configurations}
