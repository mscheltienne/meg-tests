from __future__ import annotations  # c.f. PEP 563, PEP 649

from typing import TYPE_CHECKING
from warnings import warn

from mne import Projection
from mne._fiff.constants import FIFF
from mne._fiff.tag import _rename_list
from mne._fiff.write import (
    end_block,
    start_and_end_file,
    start_block,
    write_float,
    write_float_matrix,
    write_int,
    write_name_list_sanitized,
    write_string,
)

from ..utils._checks import check_type, ensure_path
from ..utils._docs import fill_doc

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Optional, Union


def _write_proj(
    fid,
    projs: Union[list[Projection], tuple[Projection]],
    *,
    ch_names_mapping: Optional[dict[str, str]] = None,
) -> None:
    """Write a projection operator to a file.

    Parameters
    ----------
    fid : file
        The file descriptor of the open file.
    projs : dict
        The projection operator.
    """
    ch_names_mapping = dict() if ch_names_mapping is None else ch_names_mapping
    check_type(projs, (list, tuple), "projs")
    if len(projs) == 0:
        raise ValueError("The list of projectors is empty.")
    for k, proj in enumerate(projs):
        check_type(proj, Projection, f"projs[{k}]")
    check_type(ch_names_mapping, dict, "ch_names_mapping")
    for key, value in ch_names_mapping.items():
        check_type(key, str, "ch_names_mapping[key]")
        check_type(value, str, "ch_names_mapping[value]")
    start_block(fid, FIFF.FIFFB_PROJ)
    for proj in projs:
        start_block(fid, FIFF.FIFFB_PROJ_ITEM)
        write_int(fid, FIFF.FIFF_NCHAN, len(proj["data"]["col_names"]))
        names = _rename_list(proj["data"]["col_names"], ch_names_mapping)
        write_name_list_sanitized(
            fid, FIFF.FIFF_PROJ_ITEM_CH_NAME_LIST, names, "col_names"
        )
        write_string(fid, FIFF.FIFF_NAME, proj["desc"])
        write_int(fid, FIFF.FIFF_PROJ_ITEM_KIND, proj["kind"])
        if proj["kind"] == FIFF.FIFFV_PROJ_ITEM_FIELD:
            write_float(fid, FIFF.FIFF_PROJ_ITEM_TIME, 0.0)
        write_int(fid, FIFF.FIFF_PROJ_ITEM_NVEC, proj["data"]["nrow"])
        write_float_matrix(fid, FIFF.FIFF_PROJ_ITEM_VECTORS, proj["data"]["data"])
        end_block(fid, FIFF.FIFFB_PROJ_ITEM)
    end_block(fid, FIFF.FIFFB_PROJ)


@fill_doc
def write_proj(
    fname: Union[str, Path],
    projs: Union[list[Projection], tuple[Projection]],
    *,
    overwrite: bool = False,
    verbose: Optional[Union[bool, str, int]] = None,
) -> None:
    """Write projections to a FIF file.

    Parameters
    ----------
    fname : path-like
        The name of file containing the projections vectors. It should end with
        ``-proj.fif`` or ``-proj.fif.gz``.
    projs : list
        The list of projection vectors.
    overwrite : bool
        If True, overwrite the destination file (if it exists).
    %(verbose)s

    See Also
    --------
    :func:`mne.read_proj`
    """
    fname = ensure_path(fname, overwrite=overwrite)
    ensure_path(fname, must_exist=False)
    if not fname.name.endswith(
        ("-proj.fif", "-proj.fif.gz", "_proj.fif", "_proj.fif.gz")
    ):
        warn(
            "The file name should end with '-proj.fif' or '-proj.fif.gz'.",
            RuntimeWarning,
            stacklevel=2,
        )
    with start_and_end_file(fname) as fid:
        _write_proj(fid, projs)
