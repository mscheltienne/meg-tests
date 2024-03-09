from pathlib import Path as Path

import numpy as np
from numpy.typing import NDArray as NDArray

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
