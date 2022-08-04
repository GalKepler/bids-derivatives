from pathlib import Path
from typing import Union

from bids import BIDSLayout, BIDSLayoutIndexer

from bids_derivatives.derivative.messages import INVALID_ROOT


class DerivativeLayout(BIDSLayout):
    """
    A child class of *BIDSLayout* with functionalities
    specific to BIDS-Apps' outputs.
    """

    def __init__(
        self,
        root: Union[Path, str] = None,
        validate: bool = True,
        absolute_paths: bool = True,
        config: Union[str, list] = "derivatives",
        sources: Union[BIDSLayout, str] = None,
        regex_search: bool = False,
        database_path: Union[Path, str] = None,
        reset_database: bool = False,
        indexer: BIDSLayoutIndexer = None,
        **indexer_kwargs,
    ):
        """
        Instantiate a BIDSLayout object.

        Parameters
        ----------
        root : str
            The root directory of the derivative(s)' dataset.
        validate : bool, optional
            If True, all files are checked for BIDS compliance when first indexed, # noqa: E501
            and non-compliant files are ignored. This provides a convenient way to # noqa: E501
            restrict file indexing to only those files defined in the "core" BIDS # noqa: E501
            spec, as setting validate=True will lead files in supplementary folders # noqa: E501
            like derivatives/, code/, etc. to be ignored.
        absolute_paths : bool, optional
            If True, queries always return absolute paths.
            If False, queries return relative paths (for files and
            directories).
        config : str or list or None, optional
            Optional name(s) of configuration file(s) to use.
            By default (None), uses 'derivatives'.
        sources : :obj:`bids.layout.BIDSLayout` or list or None, optional
            Optional BIDSLayout(s) from which the current BIDSLayout is derived.
        regex_search : bool
            Whether to require exact matching (True) or regex
            search (False, default) when comparing the query string to each
            entity in .get() calls. This sets a default for the instance, but
            can be overridden in individual .get() requests.
        database_path : str
            Optional path to directory containing SQLite database file index
            for this BIDS dataset. If a value is passed and the folder
            already exists, indexing is skipped. By default (i.e., if None),
            an in-memory SQLite database is used, and the index will not
            persist unless .save() is explicitly called.
        reset_database : bool
            If True, any existing directory specified in the
            database_path argument is deleted, and the BIDS dataset provided
            in the root argument is reindexed. If False, indexing will be
            skipped and the existing database file will be used. Ignored if
            database_path is not provided.
        indexer: BIDSLayoutIndexer or callable
            An optional BIDSLayoutIndexer instance to use for indexing, or any
            callable that takes a BIDSLayout instance as its only argument. If
            None, a new indexer with default parameters will be implicitly created.
        indexer_kwargs: dict
            Optional keyword arguments to pass onto the newly created
            BIDSLayoutIndexer. Valid keywords are 'ignore', 'force_index',
            'index_metadata', and 'config_filename'. Ignored if indexer is not
            None.
        """
        is_derivative = self.parse_root_directory(root)
        super().__init__(
            root=root,
            validate=validate,
            absolute_paths=absolute_paths,
            config=config,
            sources=sources,
            regex_search=regex_search,
            database_path=database_path,
            reset_database=reset_database,
            indexer=indexer,
            derivatives=is_derivative,
            **indexer_kwargs,
        )

    def parse_root_directory(self, root: Union[Path, str]) -> bool:
        """
        Parse the root directory of the derivative(s)' dataset.
        Make sure that the root either contains a 'derivatives' folder,
        or that the root is a derivative's folder.

        Parameters
        ----------
        root : Union[Path, str]
            The root directory of the derivative(s)' dataset.


        Returns
        -------
        bool
            True if the root contains a derivative's folder, False otherwise.

        Raises
        ------
        ValueError
            If the root is not a derivative's folder and doesn't contain one.
        """
        root = Path(root)
        if root.parent.name == "derivatives":
            return False
        else:
            if (root / "derivatives").exists():
                return True
            else:
                raise ValueError(INVALID_ROOT)
