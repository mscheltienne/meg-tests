from __future__ import annotations

from importlib.resources import files
from pathlib import Path
from typing import TYPE_CHECKING

import pooch

from ..utils._checks import ensure_path
from ._fetch import fetch_dataset

if TYPE_CHECKING:
    from typing import Optional, Union

_REGISTRY: Path = files("meg_wiki.datasets") / "sample-registry.txt"


def _make_registry(
    folder: Union[str, Path], output: Optional[Union[str, Path]] = None
) -> None:
    """Create the registry file for the sample dataset.

    Parameters
    ----------
    folder : path-like
        Path to the sample dataset.
    output : path-like
        Path to the output registry file.
    """
    folder = ensure_path(folder, must_exist=True)
    output = _REGISTRY if output is None else ensure_path(output, must_exist=False)
    files = sorted(
        [
            file
            for file in folder.glob("**/*")
            if file.is_file()
            and file.relative_to(folder).parts[0] != ".git"
            and not file.name.startswith(".git")
            and not file.name == "version.txt"
        ]
    )
    hashes = [pooch.file_hash(file) for file in files]
    with open(output, "w") as outfile:
        for fname, fhash in zip(files, hashes):
            outfile.write(f"{fname.relative_to(folder).as_posix()} {fhash}\n")


def data_path() -> Path:
    """Return the path to the sample dataset, downloaded if needed.

    Returns
    -------
    path : Path
        Path to the sample dataset, by default in ``"~/meg-wiki_data"``.
    """
    path = Path.home() / "meg-wiki_data"
    base_url = "https://github.com/fcbg-hnp-meeg/meg-wiki-datasets/raw/main/"
    registry = files("meg_wiki.datasets") / "sample-registry.txt"
    return fetch_dataset(path, base_url, registry)
