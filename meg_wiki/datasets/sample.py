from __future__ import annotations  # c.f. PEP 563 and PEP 649

from importlib.resources import files
from typing import TYPE_CHECKING

import pooch

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Union


def _make_registry(output: Union[str, Path]) -> None:
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
    pooch.make_registry(folder, output=output, recursive=True)
