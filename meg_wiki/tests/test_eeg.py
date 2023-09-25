import pytest
from mne import create_info

from meg_wiki.datasets import sample
from meg_wiki.eeg import load_mapping


directory = sample.data_path() / "eeg-layout"


@pytest.mark.parametrize("n", (32, 64, 128))
def test_mapping(n) -> None:
    """Test that all 3 mapping match the standard 10/05 naming."""
    fname = directory / f"mapping-eeg-{n}-chs.txt"
    mapping = load_mapping(fname)
    info = create_info(list(mapping.values()), 1000, "eeg")
    info.set_montage("standard_1005")
