import warnings
from pathlib import Path
from typing import Union

import parse


class SingleSubjectDerivative:
    """
    A SingleDerivative is a class that perform queries on the BIDS-App at a single participant level.
    """

    #: Template
    SUBJECT_TEMPLATE = "sub-{subject}"

    def __init__(self, base_dir: Union[str, Path], participant_label: str = None):
        self.base_dir, self.participant_label = self.validate_participant_label(Path(base_dir), participant_label)

    @staticmethod
    def validate_participant_label(base_dir: Path, participant_label: str = None):
        """
        Validate the participant label from either a subject-specific directory or a specified label.

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
        if participant_label is not None:
            parser = parse.parse(SingleSubjectDerivative.SUBJECT_TEMPLATE, participant_label)
            if parser:
                participant_label = parser.named.get("subject")
            else:
                pass  # Keep participant label as is.
        base_dir_name = base_dir.name
        parser = parse.parse(SingleSubjectDerivative.SUBJECT_TEMPLATE, base_dir_name)
        if parser:
            base_dir = base_dir.parent
            if not participant_label:
                participant_label = parser.named.get("subject")
            else:
                if participant_label != parser.named.get("subject"):
                    warnings.warn(f"Participant label {participant_label} does not match the base directory name {base_dir_name}.")

        return base_dir, participant_label
