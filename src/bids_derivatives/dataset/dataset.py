from pathlib import Path
from typing import Union


class BIDSDerivative:
    #: Templates

    def __init__(self, base_directory: Union[str, Path]) -> None:
        self.base_directory = self.validate_base_dir(base_directory)

    @staticmethod
    def validate_base_directory(base_directory: Union[str, Path]) -> Path:
        """
        Validate the base directory.
        """
        if isinstance(base_directory, str):
            base_directory = Path(base_directory)
        if not base_directory.exists():
            raise ValueError(
                "Base directory {base_directory} does not exist.".format(
                    base_directory=base_directory
                )
            )
        return base_directory
