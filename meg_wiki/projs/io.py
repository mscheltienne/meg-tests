from __future__ import annotations  # c.f. PEP 563, PEP 649

from copy import deepcopy
from typing import TYPE_CHECKING
from warnings import warn

from mne import Projection
from mne._fiff.constants import FIFF
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

from ..utils._checks import check_type, check_value, ensure_int, ensure_path
from ._utils import orthonormalize_proj, rename_proj

if TYPE_CHECKING:
    from pathlib import Path
    from typing import IO, Union


def _write_proj(
    fid: IO,
    projs: list[Projection],
) -> None:
    """Write a projection operator to a file.

    Parameters
    ----------
    fid : file
        The file descriptor of the open file.
    projs : list of Projection
        The projection operators.
    """
    start_block(fid, FIFF.FIFFB_PROJ)
    for proj in projs:
        start_block(fid, FIFF.FIFFB_PROJ_ITEM)
        write_int(fid, FIFF.FIFF_NCHAN, len(proj["data"]["col_names"]))
        write_name_list_sanitized(
            fid,
            FIFF.FIFF_PROJ_ITEM_CH_NAME_LIST,
            proj["data"]["col_names"],
            "col_names",
        )
        write_string(fid, FIFF.FIFF_NAME, proj["desc"])
        write_int(fid, FIFF.FIFF_PROJ_ITEM_KIND, proj["kind"])
        if proj["kind"] == FIFF.FIFFV_PROJ_ITEM_FIELD:
            write_float(fid, FIFF.FIFF_PROJ_ITEM_TIME, 0.0)
        write_int(fid, FIFF.FIFF_PROJ_ITEM_NVEC, proj["data"]["nrow"])
        write_float_matrix(fid, FIFF.FIFF_PROJ_ITEM_VECTORS, proj["data"]["data"])
        end_block(fid, FIFF.FIFFB_PROJ_ITEM)
    end_block(fid, FIFF.FIFFB_PROJ)


def write_proj(
    fname: Union[str, Path],
    projs: Union[list[Projection], tuple[Projection]],
    position: int,
    *,
    overwrite: bool = False,
    orthonormalize: bool = False,
) -> None:
    """Write projections to a FIF file.

    The projectors only contain the required tags for the DACQ. MNE tags are removed.

    Parameters
    ----------
    fname : path-like
        The name of file containing the projections vectors. It should end with
        ``-proj.fif`` or ``-proj.fif.gz``.
    projs : list
        The list of projection vectors.
    position : int
        Gantry position in degree: ``0``, ``60`` or ``68``.
    overwrite : bool
        If True, overwrite the destination file (if it exists).
    orthonormalize : bool
        If True, the projectors are transformed to form an orthonormal basis using
        :func:`scipy.linalg.orth`.

    See Also
    --------
    :func:`mne.read_proj`
    """
    fname = ensure_path(fname, must_exist=False)
    check_type(projs, (list, tuple), "projs")
    if len(projs) == 0:
        raise ValueError("The list of projectors is empty.")
    for k, proj in enumerate(projs):
        check_type(proj, (Projection,), f"projs[{k}]")
    position = ensure_int(position, "position")
    check_value(position, (0, 60, 68), "position")
    check_type(overwrite, (bool,), "overwrite")
    check_type(orthonormalize, (bool,), "orthonormalize")
    if fname.exists() and not overwrite:
        raise FileExistsError(f"The file {fname} already exists.")
    if not fname.name.endswith(
        ("-proj.fif", "-proj.fif.gz", "_proj.fif", "_proj.fif.gz")
    ):
        warn(
            "The file name should end with '-proj.fif' or '-proj.fif.gz'.",
            RuntimeWarning,
            stacklevel=2,
        )
    projs = list(deepcopy(projs))
    if orthonormalize:
        projs = orthonormalize_proj(projs)
    projs = rename_proj(projs, position, combined=orthonormalize)
    with start_and_end_file(fname) as fid:
        _write_proj(fid, projs)
