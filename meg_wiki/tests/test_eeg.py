from __future__ import annotations  # c.f. PEP 563, PEP 649

from importlib.resources import files
from typing import TYPE_CHECKING

import pytest
from mne import create_info

from meg_wiki.datasets import sample
from meg_wiki.eeg import (
    load_mapping,
    load_mapping_32chs,
    load_mapping_64chs,
    load_mapping_128chs,
)
from meg_wiki.utils._tests import sha256sum

if TYPE_CHECKING:
    from typing import Callable

directory = sample.data_path() / "eeg-layout"


@pytest.mark.parametrize("n", (32, 64, 128))
def test_mapping(n: int) -> None:
    """Test that all 3 mapping match the standard 10/05 naming."""
    fname = directory / f"mapping-eeg-{n}-chs.txt"
    mapping = load_mapping(fname)
    info = create_info(list(mapping.values()), 1000, "eeg")
    info.set_montage("standard_1005")


@pytest.mark.parametrize(
    "n, func",
    [(32, load_mapping_32chs), (64, load_mapping_64chs), (128, load_mapping_128chs)],
)
def test_mapping_sync(n: int, func: Callable) -> None:
    """Test that the asset folder is in sync with the sample dataset."""
    fname = directory / f"mapping-eeg-{n}-chs.txt"
    assert load_mapping(fname) == func()
    fname2 = files("meg_wiki") / "assets" / "eeg-layout" / f"mapping-eeg-{n}-chs.txt"
    assert sha256sum(fname) == sha256sum(fname2)
