import json
import logging
from pathlib import Path
from typing import Union

from bids_derivatives.dataset.messages import (
    BASE_DIRECTORY_MISSING,
    DATASET_DESCRIPTION_MESSAGES,
)
from bids_derivatives.dataset.utils import query_dataset_description
from bids_derivatives.utils.logs import LOGGER_CONFIG


class BIDSDerivative:
    #: Templates

    def __init__(
        self, base_directory: Union[str, Path], verbosity: Union[str, int] = 0
    ) -> None:
        self.base_directory = self.validate_base_directory(base_directory)
        self.logger = self.set_logger(verbosity=verbosity)

    def set_logger(self, verbosity: Union[str, int] = 0):
        logger = logging.getLogger(__name__)
        logging.basicConfig(**LOGGER_CONFIG)
        verbosity = (
            getattr(logging, verbosity.upper(), None)
            if isinstance(verbosity, str)
            else verbosity
        )
        logger.setLevel(verbosity)
        return logger

    def validate_base_directory(
        self, base_directory: Union[str, Path]
    ) -> Path:
        """
        Validate the base directory.
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
