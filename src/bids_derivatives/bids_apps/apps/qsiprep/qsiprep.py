from ctypes import Union
from pathlib import Path

from bids_derivatives.derivative import SingleSubjectDerivative


class QSIPrepDerivative(SingleSubjectDerivative):
    def __init__(
        self,
        base_directory: Union[str, Path],
        participant_label: str = None,
        exists: bool = True,
    ):
        super().__init__(base_directory, participant_label, exists)
