from pathlib import Path as Path
from typing import IO, Optional, Union

from mne import Projection

from ..utils._checks import check_type as check_type
from ..utils._checks import ensure_path as ensure_path
from ..utils._docs import fill_doc as fill_doc

def _write_proj(
    fid: IO,
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

def write_proj(
    fname: Union[str, Path],
    projs: Union[list[Projection], tuple[Projection]],
    *,
    overwrite: bool = False,
    verbose: Optional[Union[bool, str, int]] = None,
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
    overwrite : bool
        If True, overwrite the destination file (if it exists).
    verbose : int | str | bool | None
        Sets the verbosity level. The verbosity increases gradually between ``"CRITICAL"``,
        ``"ERROR"``, ``"WARNING"``, ``"INFO"`` and ``"DEBUG"``. If None is provided, the
        verbosity is set to ``"WARNING"``. If a bool is provided, the verbosity is set to
        ``"WARNING"`` for False and to ``"INFO"`` for True.

    See Also
    --------
    :func:`mne.read_proj`
    """
