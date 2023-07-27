from __future__ import annotations  # c.f. PEP 563 and PEP 649

from importlib.resources import files
from pathlib import Path
from typing import TYPE_CHECKING

import pooch

if TYPE_CHECKING:
    from typing import Optional, Union


def _make_registry(output: Optional[Union[str, Path]] = None) -> None:
    """Create the registry file for the sample dataset.

    Parameters
    ----------
    output : str | Path
        Path to the output registry file.
    """
    folder = files("meg_wiki").parent / "datasets"
    if not folder.exists():
        raise RuntimeError(
            "The sample dataset registry can only be created from a clone of the "
            "repository."
        )
    output = (
        files("meg_wiki.datasets") / "sample-registry.txt" if output is None else output
    )
    pooch.make_registry(folder, output=output, recursive=True)


def data_path() -> Path:
    """Return the path to the sample dataset, downloaded if needed.

    Returns
    -------
    path : Path
        Path to the sample dataset, by default in "~/meg-wiki_data".
    """
    fetcher = pooch.create(
        path=Path.home() / "meg-wiki_data",
        base_url="https://github.com/fcbg-hnp-meeg/meg-wiki/raw/main/datasets/",
        registry=None,
        retry_if_failed=2,
        allow_updates=True,
    )
    fetcher.load_registry(files("meg_wiki.datasets") / "sample-registry.txt")
    for file in fetcher.registry:
        fetcher.fetch(file)
    return fetcher.abspath
