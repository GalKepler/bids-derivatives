import logging
from typing import Union

LOGGER_CONFIG = dict(
    filemode="w",
    format="%(asctime)s %(name)-12s - %(levelname)-8s %(message)s",
)


def set_logger(name: str, verbosity: Union[str, int] = 0):
    """


    Parameters
    ----------
    verbosity : Union[str, int], optional
        _description_, by default 0

    Returns
    -------
    _type_
        _description_
    """
    logger = logging.getLogger(name)
    logging.basicConfig(**LOGGER_CONFIG)
    verbosity = (
        getattr(logging, verbosity.upper(), None)
        if isinstance(verbosity, str)
        else verbosity
    )
    logger.setLevel(verbosity)
    return logger
