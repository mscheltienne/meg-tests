"""
.. _tut-sensor-positions:

Sensor positions
================

.. note::

    This example requires the ``meg_wiki`` package to download the sample dataset. This
    package can be installed with ``pip``:

    .. code-block:: bash

        pip install git+https://github.com/fcbg-hnp-meeg/meg-wiki

The sensor position is defined for each sensors as an `~numpy.array` of 12 elements.
This array represents the position and the normal given by a ``(3, 3)`` rotation matrix,
in device coordinates.
"""

from mne.io.meas_info import read_info

from meg_wiki.datasets import sample


info = read_info(
    sample.data_path() / "meas_info" / "measurement-info.fif", verbose=False
)
info

# %%
# In MNE-Python, the sensor position is stored under the key ``loc`` for every channels.

print(info["chs"][0]["loc"])

# %%
# Along with other sensor information:

for key, value in info["chs"][0].items():
    if key == "loc":
        print(f"{key}:\n  Position:\n{value[:3]}\n  Normal:\n{value[3:].reshape(3, 3)}")
    else:
        print(f"{key}: {value}")

# %%
# The sensors can be visualized on a 3D plot. This measurement information was taken
# from an empty-room recording. Thus, it does not contain an HPI measurement and it does
# not contain the transform from the device to the head coordinate frame.

from matplotlib import pyplot as plt
from mne.transforms import Transform
from mne.viz import plot_sensors

# set an identity transformation from the device to head coordinates
info["dev_head_t"] = Transform("meg", "head")
ax = plt.axes(projection="3d")
plot_sensors(info, kind="3d", axes=ax)
ax.view_init(azim=130, elev=20)
plt.show()

# %%
# The 3D coordinates can be projected on a 2D plane to represent a topographic view of
# the sensor array. In MNE, a :class:`~mne.channels.Layout` object is used to represent
# the idealied 2D sensor positions. Built-in layouts are available for the MEGIN system,
# under the keys ``'Vectorview-all'``, ``'Vectorview-mag'``, ``'Vectorview-grad'``, and
# ``'Vectorview-grad_norm'``.

import numpy as np
from mne.channels import read_layout

layout = read_layout("Vectorview-all")
fig, ax = plt.subplots(1, 1, figsize=(16.53, 11.69), layout="constrained")
ax.set(xticks=[], yticks=[], aspect="equal")
outlines = dict(border=([0, 1, 1, 0, 0], [0, 0, 1, 1, 0]))
for p, ch_name in zip(layout.pos, layout.names):
    center_pos = np.array((p[0] + p[2] / 2.0, p[1] + p[3] / 2.0))
    ch_name = ch_name.split("MEG")[1]
    ch_name = f"MAG\n{ch_name}" if ch_name.endswith("1") else f"GRAD\n{ch_name}"
    ax.annotate(
        ch_name,
        xy=center_pos,
        horizontalalignment="center",
        verticalalignment="center",
        size=6,
    )
    x1, x2, y1, y2 = p[0], p[0] + p[2], p[1], p[1] + p[3]
    ax.plot([x1, x1, x2, x2, x1], [y1, y2, y2, y1, y1], color="k")
ax.axis("off")
plt.show()

# %%
# .. note::
#
#    The function :func:`mne.viz.plot_layout` or the method :meth:`mne.Layout.plot` can
#    be used to plot the layout faster without customization.
