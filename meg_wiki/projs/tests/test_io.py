from shutil import copyfile

import numpy as np
import pytest
from mne import read_proj
from mne._fiff.open import fiff_open
from numpy.testing import assert_allclose

from meg_wiki.datasets import sample
from meg_wiki.projs import write_proj

# c.f. https://github.com/mne-tools/fiff-constants/blob/master/DictionaryTags.txt
_TAGS: set[int] = {
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
        write_proj(tmp_path / "test.fif", projs, position=68)
    write_proj(tmp_path / "test_proj.fif", projs, position=68)
    # reload and compare
    with pytest.warns(RuntimeWarning, match="does not conform to MNE naming"):
        projs1 = read_proj(tmp_path / "test.fif")
    projs2 = read_proj(tmp_path / "test_proj.fif")
    assert projs1 == projs2
    # manually compare the main fields
    for p1, p2 in zip(projs, projs1, strict=True):
        assert p1["desc"] + "_68deg" == p2["desc"]
        assert p1["kind"] == p2["kind"]
        assert p1["data"]["nrow"] == p2["data"]["nrow"]
        assert p1["data"]["ncol"] == p2["data"]["ncol"]
        assert p1["data"]["row_names"] == p2["data"]["row_names"]
        assert p1["data"]["col_names"] == p2["data"]["col_names"]
        assert_allclose(p1["data"]["data"], p2["data"]["data"])
    # check presence and absence of FIFF tags
    fid, tree, _ = fiff_open(tmp_path / "test_proj.fif")
    projs = tree["children"][0]["children"]
    for proj in projs:
        tags = [tag.kind for tag in proj["directory"]]
        assert set(tags) == _TAGS
        assert len(tags) == len(_TAGS)
    fid.close()


def test_write_proj_invalid(tmp_path):
    """Test writing projectors with invalid arguments."""
    with pytest.raises(TypeError, match="provided path"):
        write_proj(101, [], position=0)
    with pytest.raises(ValueError, match="list of projectors is empty"):
        write_proj(tmp_path / "test_proj.fif", [], position=0)
    with pytest.raises(TypeError, match="must be an instance of"):
        write_proj(tmp_path / "test_proj.fif", "foo", position=0)
    with pytest.raises(TypeError, match="must be an instance of"):
        write_proj(tmp_path / "test_proj.fif", ["foo"], position=0)
    fname = sample.data_path() / "ssp" / "200123" / "ssp_68_200123_proj.fif"
    projs = read_proj(fname)
    with pytest.raises(TypeError, match="must be an integer"):
        write_proj(tmp_path / "test_proj.fif", projs, position="101")
    with pytest.raises(ValueError, match="Allowed values are"):
        write_proj(tmp_path / "test_proj.fif", projs, position=101)
    with pytest.raises(TypeError, match="must be an instance of"):
        write_proj(tmp_path / "test_proj.fif", projs, position=0, overwrite="True")
    with pytest.raises(TypeError, match="must be an instance of"):
        write_proj(
            tmp_path / "test_proj.fif",
            projs,
            position=0,
            overwrite=False,
            orthonormalize="True",
        )
    assert not (tmp_path / "test_proj.fif").exists()


def test_write_proj_overwrite(tmp_path):
    """Test overwriting existing projectors."""
    fname = sample.data_path() / "ssp" / "200123" / "ssp_68_200123_proj.fif"
    projs = read_proj(fname)
    copyfile(fname, tmp_path / "test_proj.fif")
    with pytest.raises(FileExistsError, match="already exists"):
        write_proj(tmp_path / "test_proj.fif", projs, position=0)
    assert projs[0]["desc"] != "test"
    projs[0]["desc"] = "test"
    assert projs[0]["desc"] == "test"
    write_proj(tmp_path / "test_proj.fif", projs, position=0, overwrite=True)
    assert (tmp_path / "test_proj.fif").exists()
    projs = read_proj(tmp_path / "test_proj.fif")
    assert projs[0]["desc"] == "test_0deg"  # position is appended to the proj name


def test_write_orthonormalized_proj(tmp_path):
    """Test writing of orthonormalized projectors."""
    fname = sample.data_path() / "ssp" / "200123" / "ssp_68_200123_proj.fif"
    projs = read_proj(fname)
    write_proj(tmp_path / "test_proj.fif.gz", projs, position=68, orthonormalize=True)
    projs_ortho = read_proj(tmp_path / "test_proj.fif.gz")
    # check names
    for k, proj in enumerate(projs_ortho):
        assert proj["desc"] == f"ssp_combined_{k}_68deg"
    # check data and orthonormality, shape of (n_channels, n_projs)
    data = np.array([proj["data"]["data"].squeeze() for proj in projs]).T
    data_ortho = np.array([proj["data"]["data"].squeeze() for proj in projs_ortho]).T
    assert not np.allclose(data, data_ortho)
    assert_allclose(
        np.linalg.norm(data_ortho, axis=0), np.ones(data_ortho.shape[1]), atol=1e-6
    )
    assert_allclose(data_ortho.T @ data_ortho, np.eye(data_ortho.shape[1]), atol=1e-6)
