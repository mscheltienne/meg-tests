from pathlib import Path
from typing import Optional, Union

from ._fetch import fetch_dataset as fetch_dataset

def _make_registry(output: Optional[Union[str, Path]] = None) -> None:
    """Create the registry file for the sample dataset.

    Parameters
    ----------
    output : str | Path
        Path to the output registry file.
    """

def data_path() -> Path:
    """Return the path to the sample dataset, downloaded if needed.

    Returns
    -------
    path : Path
        Path to the sample dataset, by default in ``"~/meg-wiki_data"``.
    """
