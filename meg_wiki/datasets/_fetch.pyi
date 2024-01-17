from collections.abc import Generator
from pathlib import Path
from typing import Union

from ..utils._checks import ensure_path as ensure_path
from ..utils.logs import logger as logger

def fetch_dataset(path: Path, base_url: str, registry: Union[str, Path]) -> Path:
    """Fetch a dataset from the remote.

    Parameters
    ----------
    path : str | Path
        Local path where the dataset should be cloned.
    base_url : str
        Base URL for the remote data sources. All requests will be made relative to this
        URL. If the URL does not end in a '/', a trailing '/' will be added
        automatically.
    registry : str | Path
        Path to the txt file containing the registry.

    Returns
    -------
    path : Path
        Absolute path to the local clone of the dataset.
    """

def _walk(path: Path) -> Generator[Path, None, None]:
    """Walk recursively through a directory tree and yield the existing files.

    Parameters
    ----------
    path : Path
        Path to a directory.
    """
