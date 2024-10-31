from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from pathlib import Path

    from numpy.typing import NDArray


def load_fine_calibration(
    fname: str | Path,
) -> dict[str, list[str] | NDArray[np.float64] | list[NDArray[np.float64]]]:
    """Load a fine calibration.

    The fine calibration typically includes improved sensor locations,
    calibration coefficients, and gradiometer imbalance information.

    Parameters
    ----------
    fname : path-like
        Path to the ``'.dat'`` file containing the mapping to load. Each line
        yields one channels formatted.

    Returns
    -------
    calibration : dict
        Fine calibration information.

            * ch_names : list of str
                  List of the channel names.
            * locs : array of shape (n_channels, 12)
                  Coil location and orientation parameters.
            * imb_cals : list of array of shape (1,) or (3,)
                  For magnetometers, the calibration coefficients.
                  For gradiometers, one or three imbalance parameters.
    """
    with open(fname) as fid:
        lines = fid.readlines()
    lines = [
        [elt.strip() for elt in line.split("\n")[0].split(" ") if len(elt.strip()) != 0]
        for line in lines
    ]
    assert all(len(elt[0]) in (3, 4) for elt in lines)  # sanity-check

    ch_names, locs, imb_cals = list(), list(), list()
    for elt in lines:
        ch_names.append("MEG" + elt[0].zfill(4))
        locs.append(np.array(elt[1:13], float))
        imb_cals.append(np.array(elt[13:], float))
    locs = np.array(locs)
    return dict(ch_names=ch_names, locs=locs, imb_cals=imb_cals)
