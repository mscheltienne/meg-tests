from __future__ import annotations

import re
from typing import TYPE_CHECKING

import numpy as np
from scipy.linalg import orth

if TYPE_CHECKING:
    from mne import Projection


def orthonormalize_proj(
    projs: list[Projection],
) -> list[Projection]:
    """Transform the set of projector vectors into an orthonormal basis using SVD.

    Parameters
    ----------
    projs : list of Projection
        The projection operators.

    Returns
    -------
    projs : list of Projection
        The orthogonalized projection operators.
    """
    # each projector shape is (1, n_channels), thus data shape is (n_channels, n_projs)
    data = np.array([proj["data"]["data"].squeeze() for proj in projs]).T
    data = orth(data)  # (n_channels, n_orth_projs), n_orth_projs <= n_projs
    for k, proj_data in enumerate(data.T):
        projs[k]["data"]["data"] = proj_data.reshape(1, -1)
    projs = projs[: data.shape[1]]  # n_orth_projs
    pattern = re.compile(r"\d{1,2}deg")  # detect gantry position
    for k, proj in enumerate(projs):
        hits = re.findall(pattern, proj["desc"])
        proj["desc"] = (
            f"ssp_{hits[0]}_combined_{k}" if len(hits) == 1 else f"ssp_combined_{k}"
        )
    return projs


def rename_proj(
    projs: list[Projection], position: int, combined: bool
) -> list[Projection]:
    """Rename the projection operators.

    Parameters
    ----------
    projs : list of Projection
        The projection operators.
    position : int
        The gantry position.
    combined : bool
        Whether the projection operators are combined through an orthonormalization.
    """
    pattern = re.compile(r"\d{1,2}deg")  # detect gantry position
    for k, proj in enumerate(projs):
        if combined:
            proj["desc"] = f"ssp_combined_{k}_{position}deg"
            continue
        hits = re.findall(pattern, proj["desc"])
        if len(hits) != 1:
            proj["desc"] = proj["desc"] + f"_{position}deg"
            continue
        idx = proj["desc"].find(hits[0])
        proj["desc"] = (
            proj["desc"][:idx] + f"{position}deg" + proj["desc"][idx + len(hits[0]) :]
        )
    return projs
