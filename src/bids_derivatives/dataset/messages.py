import logging

BASE_DIRECTORY_MISSING = "Base directory {base_directory} does not exist."


def raise_required_keys_missing(keys: list, logger: logging.Logger = None):
    """
    Raise an error if the required keys are missing.
    """
    msg = "The following required keys are missing from the dataset description: {}".format(
        keys
    )
    if logger is not None:
        logger.error(msg)
    raise ValueError(msg)


def warn_recommended_keys_missing(keys: list, logger: logging.Logger = None):
    """
    Warn if the recommended keys are missing.
    """
    msg = "The following recommended keys are missing from the dataset description: {}".format(
        keys
    )
    if logger is None:
        logging.warning(msg)
    else:
        logger.warning(msg)


def notify_optional_keys_missing(keys: list, logger: logging.Logger = None):
    """
    Warn if the recommended keys are missing.
    """
    msg = "The following optional keys are missing from the dataset description: {}".format(
        keys
    )
    if logger is None:
        logging.debug(msg)
    else:
        logger.debug(msg)


DATASET_DESCRIPTION_MESSAGES = {
    "required": raise_required_keys_missing,
    "recommended": warn_recommended_keys_missing,
    "optional": notify_optional_keys_missing,
}
