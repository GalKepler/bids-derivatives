import json
from collections import defaultdict
from pathlib import Path
from typing import Union

DATASET_DESCRIPTION_KEYS = {
    "required": ["Name", "BIDSVersion"],
    "recommended": [
        "HEDVersion",
        "DatasetType",
        "License",
        "GeneratedBy",
        "SourceDatasets",
    ],
    "optional": [
        "Authors",
        "Acknowledgements",
        "HowToAcknowledge",
        "Funding",
        "EthicsApprovals",
        "ReferencesAndLinks",
        "DatasetDOI",
    ],
}


def query_dataset_description(
    dataset_description: Union[Path, str],
    dataset_description_keys: dict = DATASET_DESCRIPTION_KEYS,
) -> dict:
    """
    Query the dataset description.

    Parameters
    ----------
    dataset_description : Union[Path, str]
        Path to the dataset description json file.
    dataset_description_keys : dict, optional
        Dictionary of keys to query, by default DATASET_DESCRIPTION_KEYS

    Returns
    -------
    dict
        Dictionary of keys and values describing
        existence in the dataset description.
    """
    query = defaultdict(dict)
    dataset_description = Path(dataset_description)
    if not dataset_description.exists():
        return False
    with open(dataset_description, "r") as f:
        dataset_description_dict = json.load(f)
        for requirement, keys in dataset_description_keys.items():
            for key in keys:

                query[requirement][key] = key in dataset_description_dict
    return query
