from __future__ import annotations  # c.f. PEP 563, PEP 649

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

if TYPE_CHECKING:
    from typing import Callable

directory = sample.data_path() / "eeg-layout"


@pytest.mark.parametrize(
    "n, func",
    [(32, load_mapping_32chs), (64, load_mapping_64chs), (128, load_mapping_128chs)],
)
def test_mapping(n: int, func: Callable[[], dict[str, str]]) -> None:
    """Test that all 3 mapping match the standard 10/05 naming."""
    fname = directory / f"mapping-eeg-{n}-chs.txt"
    mapping = load_mapping(fname)
    assert mapping == func()
    info = create_info(list(mapping.values()), 1000, "eeg")
    info.set_montage("standard_1005")
