"""
.. _tut-artifact-ssp:

Create Signal Space Projectors
==============================

Background on projection
------------------------

Signal-Space Projection (SSP)\ :footcite:p:`ssp_1997` is a way of estimating a
projection matrix to remove noise from a recording by comparing measurements with and
without the signal of interest. An empty-room recording is typically used to estimate
the direction(s) of environmental noise in sensor space. Once the noise vector(s) are
known, you can create an orthogonal hyperplane and construct a projection matrix to
project your recording onto that hyperplane. It should be clear that SSP reduces the
dimensionality of your data and thus sensors will not retain linear independency.

Additional information on projections and on Signal-Space Projection (SSP) can be found
in `MNE's Python background on projectors and projections`_.

MNE's Python geometric example projecting from 3-dimensional space to the (x, y) plane:

.. _MNE's Python background on projectors and projections: https://mne.tools/stable/auto_tutorials/preprocessing/45_projectors_background.html
"""

import numpy as np
from matplotlib import pyplot as plt

ax = plt.axes(projection="3d")
ax.view_init(azim=-105, elev=20)
ax.set(xlabel="x", ylabel="y", zlabel="z", xlim=(-1, 5), ylim=(-1, 5), zlim=(0, 5))

# plot the vector (3, 2, 5)
origin = np.zeros((3, 1))
point = np.array([[3, 2, 5]]).T
vector = np.hstack([origin, point])
ax.plot(*vector, color="k")
ax.plot(*point, color="k", marker="o")

# project the vector onto the x,y plane and plot it
xy_projection_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
projected_point = xy_projection_matrix @ point
projected_vector = xy_projection_matrix @ vector
ax.plot(*projected_vector, color="C0")
ax.plot(*projected_point, color="C0", marker="o")

# add dashed arrow showing projection
arrow_coords = np.concatenate([point, projected_point - point]).flatten()
ax.quiver3D(
    *arrow_coords,
    length=0.96,
    arrow_length_ratio=0.1,
    color="C1",
    linewidth=1,
    linestyle="dashed"
)
plt.show()

#%%
# Default projectors
# ------------------
#
# The default set of projectors is available `here <ssp github_>`_, on our GitHub. Those
# projectors were obtained by taking:
#
# - For magnetometers:  6 components from the wideband PCA and 3 components from the
#   narrowband PCA, with a bandpass filter between 15 and 18 Hz.
# - For gradiometers: 3 components from the wideband PCA and 2 components from the
#   narrowband PCA, with a bandpass filter between 15 and 18 Hz.
#
# The narrowband PCA improves the correction of the 16.7 Hz artifact, typical from a
# 15 kV AC railway electrification system.
#
# Let's have a look at the projectors in 68° position when IAS is disabled.

from mne import read_proj

from meg_wiki.datasets import sample


projs = read_proj(sample.data_path() / "ssp" / "ssp_68_230120-proj.fif")

#%%
# To visualize the projector as topographic maps, we need information about the sensors
# location and orientation. Those information are stored in every raw recording.

from mne.io.meas_info import read_info


info = read_info(
    sample.data_path() / "meas_info" / "measurement-info.fif", verbose=False
)
info

#%%

from matplotlib import pyplot as plt


f, ax = plt.subplots(2, 3, figsize=(6, 6))
for k, proj in enumerate(projs[0:6]):
    proj.plot_topomap(info, axes=ax[k // 3, k % 3])
    ax[k // 3, k % 3].set_title(f"PCA-v{k+1}")
plt.suptitle("Magnetometers - Wideband PCA")

f, ax = plt.subplots(1, 3, figsize=(6, 6))
for k, proj in enumerate(projs[6:9]):
    proj.plot_topomap(info, axes=ax[k])
    ax[k].set_title(f"PCA-v{k+1}")
plt.suptitle("Magnetometers - Narrowband PCA")
plt.show()

#%%

from matplotlib import pyplot as plt


f, ax = plt.subplots(1, 3, figsize=(6, 6))
for k, proj in enumerate(projs[9:12]):
    proj.plot_topomap(info, axes=ax[k])
    ax[k].set_title(f"PCA-v{k+1}")
plt.suptitle("Gradiometers - Wideband PCA")

f, ax = plt.subplots(1, 2, figsize=(6, 6))
for k, proj in enumerate(projs[12:14]):
    proj.plot_topomap(info, axes=ax[k])
    ax[k].set_title(f"PCA-v{k+1}")
plt.suptitle("Gradiometers - Narrowband PCA")
plt.show()

#%%
# References
# ----------
#
# .. footbibliography::
#
# .. _ssp github: https://github.com/fcbg-hnp-meeg/meg-wiki/tree/main/datasets/ssp
