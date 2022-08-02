import json
from enum import Enum
from typing import Union

from pathlib2 import Path

from bids_derivatives.bids_apps.outputs.qsiprep import (
    OUTPUTS as QSIPREP_OUTPUTS,
)


class CommonOutputs(Enum):
    qsiprep = QSIPREP_OUTPUTS


def validate_outputs(
    outputs: Union[dict, Path],
    required_keys: list = ["subject_specific"],
) -> dict:
    """
    Validate that a given input is either a valid dictionary
    or a json file contains a valid one dictionary.

    Parameters
    ----------
    outputs : Union[dict, Path]
        The outputs to validate.
    required_keys : list, optional
        The required keys in the dictionary,
        by default ["subject_specific"]

    Returns
    -------
    dict
        The validated outputs.
    """
    if not outputs:
        return {}
    if isinstance(outputs, Path):  # if the input is a path
        with open(outputs, "r") as f:  # open the file and read content
            outputs = json.load(f)
    for key in required_keys:  # for each required key
        if key not in outputs:  # if the key is not in the dictionary
            raise ValueError(
                f"The outputs dictionary must contain the key '{key}'"
            )
    return outputs
