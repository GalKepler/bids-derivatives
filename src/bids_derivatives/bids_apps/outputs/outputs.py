import json
from enum import Enum
from pathlib import Path
from typing import Union

from bids_derivatives.bids_apps.outputs.qsiprep import (
    OUTPUTS as QSIPREP_OUTPUTS,
)


class CommonOutputs(Enum):
    qsiprep = QSIPREP_OUTPUTS


def validate_outputs(
    outputs: Union[dict, Path],
    required_keys: list = ["entities"],
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
        by default ["entities"]

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
    for output, values in outputs.items():  # for each required key
        for key in required_keys:  # if the key is not in the dictionary
            if key not in values:  # raise an error
                raise ValueError(
                    f"The key {key} is required, but isn't available for {output} output."  # noqa: E501
                )
    return outputs
