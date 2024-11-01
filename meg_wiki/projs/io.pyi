from pathlib import Path
from typing import IO

from mne import Projection

from ..utils._checks import check_type as check_type
from ..utils._checks import check_value as check_value
from ..utils._checks import ensure_int as ensure_int
from ..utils._checks import ensure_path as ensure_path
from ._utils import orthonormalize_proj as orthonormalize_proj
from ._utils import rename_proj as rename_proj

def _write_proj(fid: IO, projs: list[Projection]) -> None:
    """Write a projection operator to a file.

    Parameters
    ----------
    fid : file
        The file descriptor of the open file.
    projs : list of Projection
        The projection operators.
    """

def write_proj(
    fname: str | Path,
    projs: list[Projection] | tuple[Projection],
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
