from pathlib import Path
from typing import Union

import parse

from bids_derivatives.derivative.messages import PARTICIPANT_MISMATCH


class SingleSubjectDerivative:
    """
    A SingleDerivative is a class that perform queries on the
    BIDS-App at a single participant level.
    """

    #: Template
    SUBJECT_TEMPLATE = "sub-{subject}"

    def __init__(
        self, base_dir: Union[str, Path], participant_label: str = None
    ):
        self.participant_label = self.validate_participant_label(
            participant_label
        )
        self.path = self.validate_base_dir(base_dir)

    def validate_participant_label(self, participant_label: str):
        """
        Validate the participant label.
        """
        if participant_label is not None:
            parser = parse.parse(
                SingleSubjectDerivative.SUBJECT_TEMPLATE, participant_label
            )
            if parser:
                participant_label = parser.named.get("subject")
            else:
                pass  # Keep participant label as is.
        return participant_label

    def validate_base_dir(self, base_dir: Union[Path, str]):
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
        _type_
            _description_

        Raises
        ------
        ValueError
            _description_
        """
        base_dir = Path(base_dir)
        base_dir_name = base_dir.name
        parser = parse.parse(
            SingleSubjectDerivative.SUBJECT_TEMPLATE, base_dir_name
        )
        if parser:
            base_dir = base_dir.parent
            if parser:
                participant_label = parser.named.get("subject")
                if self.participant_label is not None:
                    if self.participant_label != participant_label:
                        raise ValueError(
                            PARTICIPANT_MISMATCH.format(
                                participant_label=self.participant_label,
                                base_dir_name=participant_label,
                            )
                        )
                else:
                    self.participant_label = parser.named.get("subject")

        return base_dir
