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

#%%
# In MNE-Python, the sensor position is stored under the key ``loc`` for every channels.

print (info["chs"][0]["loc"])

#%%
# Along with other sensor information:

for key, value in info["chs"][0].items():
    if key == "loc":
        print (
            f"{key}:\n  Position:\n{value[:3]}\n  Normal:\n{value[3:].reshape(3, 3)}"
        )
    else:
        print (f"{key}: {value}")

#%%
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
