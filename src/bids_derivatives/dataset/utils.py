from collections import defaultdict

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
    dataset_description: dict,
    dataset_description_keys: dict = DATASET_DESCRIPTION_KEYS,
) -> dict:
    """
    Query the dataset description.

    Parameters
    ----------
    dataset_description : dict
        The dataset description.
    dataset_description_keys : dict, optional
        Dictionary of keys to query, by default DATASET_DESCRIPTION_KEYS

    Returns
    -------
    dict
        Dictionary of keys and values describing
        existence in the dataset description.
    """
    query = defaultdict(dict)
    for requirement, keys in dataset_description_keys.items():
        for key in keys:
            query[requirement][key] = key in dataset_description
    return query
