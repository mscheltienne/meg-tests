import pytest
from mne import read_proj
from mne._fiff.open import fiff_open
from numpy.testing import assert_allclose

from meg_wiki.datasets import sample
from meg_wiki.projs import write_proj

# c.f. https://github.com/mne-tools/fiff-constants/blob/master/DictionaryTags.txt
_TAGS = {
    200,  # number of channels
    233,  # intended to be a short name
    3411,  # type of the projection definition
    3412,  # time of the field sample
    3414,  # number of projection vectors
    3415,  # projection vector
    3417,  # names of the channels of the projection vectors
}


def test_write_proj(tmp_path):
    """Test writing SSP projectors."""
    fname = sample.data_path() / "ssp" / "200123" / "ssp_68_200123_proj.fif"
    projs = read_proj(fname)
    with pytest.warns(RuntimeWarning, match="should end with"):
        write_proj(tmp_path / "test.fif", projs)
    write_proj(tmp_path / "test_proj.fif", projs)
    # reload and compare
    projs1 = read_proj(tmp_path / "test.fif")
    projs2 = read_proj(tmp_path / "test_proj.fif")
    assert projs1 == projs2
    # manually compare the main fields
    for p1, p2 in zip(projs, projs1):
        assert p1["desc"] == p2["desc"]
        assert p1["kind"] == p2["kind"]
        assert p1["data"]["nrow"] == p2["data"]["nrow"]
        assert p1["data"]["ncol"] == p2["data"]["ncol"]
        assert p1["data"]["row_names"] == p2["data"]["row_names"]
        assert p1["data"]["col_names"] == p2["data"]["col_names"]
        assert_allclose(p1["data"]["data"], p2["data"]["data"])
    # check presence and absence of FIFF tags
    _, tree, _ = fiff_open(tmp_path / "test_proj.fif")
    projs = tree["children"][0]["children"]
    for proj in projs:
        tags = [tag.kind for tag in proj["directory"]]
        assert set(tags) == _TAGS
        assert len(tags) == len(_TAGS)
