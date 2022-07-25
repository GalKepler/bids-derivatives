import json
from pathlib import Path
from typing import Union

from parse import parse

from bids_derivatives.dataset.messages import (
    BASE_DIRECTORY_MISSING,
    DATASET_DESCRIPTION_MESSAGES,
)
from bids_derivatives.dataset.utils import query_dataset_description
from bids_derivatives.derivative.derivative import SingleSubjectDerivative
from bids_derivatives.utils.logs import set_logger
from bids_derivatives.utils.templates.bids import SUBJECT_TEMPLATE


class BIDSDerivative:
    """
    A BIDSDerivative is a class that perform queries on the
    BIDS-App at a multiple-subjects level.
    """

    def __init__(
        self, base_directory: Union[str, Path], verbosity: Union[str, int] = 0
    ) -> None:
        """
        Initialize the BIDSDerivative class.

        Parameters
        ----------
        base_directory : Union[str, Path]
            The base directory of the dataset.
        verbosity : Union[str, int], optional
            The verbosity level of the logger. The default is 0.
        """
        self.base_directory = self.validate_base_directory(base_directory)
        self.logger = set_logger(name=str(self), verbosity=verbosity)

    def __repr__(self) -> str:
        """
        Represent the BIDSDerivative class.

        Returns
        -------
        str
            The representation of the BIDSDerivative class.
        """

        return f"{self.analysis_title} derivatives query"

    def validate_base_directory(
        self, base_directory: Union[str, Path]
    ) -> Path:
        """
        Validate the base directory.

        Parameters
        ----------
        base_directory : Union[str, Path]
            The base directory of the dataset.

        Returns
        -------
        Path
            The validated base directory.

        Raises
        ------
        ValueError
            If the base directory is not a valid path.
        """
        base_directory = Path(base_directory)
        if not base_directory.exists():
            raise ValueError(
                BASE_DIRECTORY_MISSING.format(base_directory=base_directory)
            )
        return base_directory

    def get_dataset_description(self) -> str:
        """
        Get the dataset description.
        """
        with open(self.dataset_description_path, "r") as f:
            dataset_description = json.load(f)
            f.close()
        return dataset_description

    def validate_dataset_description(self):
        """
        Validate the dataset description.
        """
        content = query_dataset_description(self.dataset_description)
        for severity, keys in content.items():
            missing = [key for key, value in keys.items() if not value]
            if missing:
                logging_func = DATASET_DESCRIPTION_MESSAGES[severity]
                logging_func(missing, self.logger)

    def get_available_subjects(self) -> list:
        """
        Get the available subjects.
        Available subjects must be represented as a sub-directory withing
        *self.base_directory* and follow BIDS *SUBJECT_TEMPLATE*.

        Returns
        -------
        list
            The available subjects.
        """
        return [
            parse(SUBJECT_TEMPLATE, subject.name).named["subject"]
            for subject in self.base_directory.glob(
                SUBJECT_TEMPLATE.format(subject="*")
            )
        ]

    def get_derivatives(self) -> dict:
        """
        Instantiate a SingleSubjectDerivative for each subject.

        Returns
        -------
        dict
            A dictionary with keys being the subject labels and values
            being the SingleSubjectDerivative instances.
        """
        derivatives = {}
        for subject in self.get_available_subjects():
            derivatives[subject] = SingleSubjectDerivative(
                base_directory=self.base_directory,
                participant_label=subject,
                exists=True,
            )
        return derivatives

    @property
    def dataset_description_path(self) -> Path:
        """
        Get the path to the dataset description file.
        """
        return self.base_directory / "dataset_description.json"

    @property
    def dataset_description(self) -> dict:
        """
        Get the dataset description.
        """
        return self.get_dataset_description()

    @property
    def analysis_title(self) -> str:
        """
        Get the analysis title.
        """
        return self.base_directory.name.capitalize()

    @property
    def subjects(self) -> list:
        """
        Get the available subjects.
        """
        return self.get_available_subjects()

    @property
    def derivatives(self) -> dict:
        """
        Get the available subjects' SingleSubjectDerivatives.
        """
        return self.get_derivatives()
