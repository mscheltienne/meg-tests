from __future__ import annotations  # c.f. PEP 563, PEP 649

import re
from typing import TYPE_CHECKING

import numpy as np
from scipy.linalg import orth

if TYPE_CHECKING:
    from mne import Projection


def _orthonormalize_proj(
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
