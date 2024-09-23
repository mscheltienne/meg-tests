r"""
.. _tut-cHPI:

Correct head movements with cHPI
================================

.. include:: ../../../links.inc

.. important::

    This example requires the ``meg_wiki`` package to download the sample dataset. This
    package can be installed with ``pip``:

    .. code-block:: bash

        $ pip install git+https://github.com/fcbg-platforms/meg-wiki

:ref:`Signal-Space Separation (SSS) and Maxwell filter
<data-analysis-pc:MaxWell filter>`\ :footcite:p:`sss_2005,tsss_2006` can be used to
compensate for head movements during a recording. To run SSS, you can use either MEGIN's
software on the :ref:`DANA <data-analysis-pc:MEGIN's software>` or
`MNE-Python <mne stable_>`_'s implementation.

.. tip::

    The enhanced version available in `MNE-Python <mne stable_>`_ is recommended. See
    :func:`mne.preprocessing.maxwell_filter`. The fine calibration file and the
    cross-talk correction are available in the `sample dataset`_ (
    see :func:`meg_wiki.datasets.sample.data_path`).
"""

from pathlib import Path

from matplotlib import pyplot as plt
from mne.chpi import (
    compute_chpi_amplitudes,
    compute_chpi_locs,
    compute_head_pos,
    filter_chpi,
)
from mne.datasets import fetch_fsaverage
from mne.io import read_raw_fif
from mne.preprocessing import maxwell_filter
from mne.viz import plot_alignment, plot_head_positions, set_3d_view

from meg_wiki.datasets import sample

# %%
# Head Position Indicator (HPI)
# -----------------------------
#
# :ref:`Head Position Indication (HPI) <meg-session:HPI measurement>` is a technique to
# measure the head position with respect to the MEG sensors. 5 coils are placed on the
# participant head and digitized (see this
# :ref:`section about digitization <meg-session:Digitization>`) in the head coordinate
# frame. At the beginning of a recording, an electromagnetic pulse is delivered on the 5
# coils at 5 unique frequencies. The coil position with respect to the MEG sensors is
# estimated by measuring the magnetic field produced by this pulse on the MEG sensors.
#
# The initial HPI measurement is used to determine the device to head affine
# transformation matrix stored in ``raw.info["dev_head_t"]``.

raw = read_raw_fif(
    sample.data_path() / "recordings" / "sample-chpi-raw.fif", preload=True
)
raw.info["dev_head_t"]

# %%
# The initial head position can be visualized within the sensor helmet with
# :func:`mne.viz.plot_alignment`.
#
# .. note::
#
#     The figure below uses fsaverage MRI from `MNE-Python <mne stable_>`_'s dataset,
#     which does not correspond to the subject in the ``raw`` recording. In practice,
#     the subject's individual MRI should be used.

subjects_dir = Path(fetch_fsaverage()).parent
fig = plot_alignment(
    raw.info,
    trans="fsaverage",
    subject="fsaverage",
    subjects_dir=subjects_dir,
    surfaces="head-dense",
    meg=("helmet", "sensors"),
    dig="fiducials",
    show_axes=True,
)
set_3d_view(fig, 35, 70, distance=0.6, focalpoint=(0.0, 0.0, 0.0))

# %%
# continuous Head Position Indicator (cHPI)
# -----------------------------------------
#
# If the recording is short, if the participant behaves and is focused on the task, one
# can assume that the head remained still during the recording. In this case, the
# initial device to head transformation estimated during the HPI measurement can be
# assumed to be constant.
#
# cHPI is a technique to continuously monitor the head position during the recording,
# useful when the previous assumption does not hold. When cHPI is enabled, the 5 HPI
# coils are continuously excited at 5 unique frequencies. The magnetic field produced by
# the coils is measured by the MEG sensors alongside brain activity.

fig = raw.plot(
    duration=4,
    n_channels=10,
    scalings=dict(grad=4e-10),
    show_scrollbars=False,
    show_scalebars=False,
)
fig.axes[0].axvline(1.492, color="darkgreen", linestyle="--")
fig.axes[0].text(
    1.492 - 0.992, fig.axes[0].get_ylim()[0] * 0.05, "cHPI OFF", fontsize=18
)
fig.axes[0].text(1.492 + 1.1, fig.axes[0].get_ylim()[0] * 0.05, "cHPI ON", fontsize=18)
plt.show()

# %%

raw.compute_psd(fmin=280, fmax=340).plot()
plt.show()

# %%
# The signal produced by the HPI coils can be used to estimate the position of the 5
# emitting coils at different time points, and thus to track the time-varying head
# position.

# %%
# Estimating the head position
# ----------------------------
#
# In `MNE-Python <mne stable_>`_, the head position is estimated through 3 steps:
#
# - Estimate the cHPI amplitudes with :func:`mne.chpi.compute_chpi_amplitudes`
# - Estimate the cHPI positions with :func:`mne.chpi.compute_chpi_locs`
# - Estimate the head position with :func:`mne.chpi.compute_head_pos`
#
# .. note::
#
#     The function :func:`mne.chpi.compute_head_pos` returns an array of shape
#     ``(n_pos, 10)`` containing the translations as ``(x, y, z)`` and the rotations as
#     quaternions ``(q1, q2, q3)``. The translations and rotations can be converted to
#     translation and rotation matrixes with :func:`mne.chpi.head_pos_to_trans_rot_t`.

chpi_amplitudes = compute_chpi_amplitudes(raw)
chpi_locs = compute_chpi_locs(raw.info, chpi_amplitudes)
head_pos = compute_head_pos(raw.info, chpi_locs)

# %%
# The estimated head position can be plotted in function of time with
# :func:`mne.viz.plot_head_positions`.

plot_head_positions(head_pos, mode="traces")
plot_head_positions(head_pos, mode="field")
plt.show()

# %%
# Compensate head movements
# -------------------------
#
# Now that the head position at different timepoints, this information can be used to
# compensate for the head movements during the recording. The function
# :func:`mne.preprocessing.maxwell_filter` uses the returned head positions in the
# argument ``head_pos`` to apply the compensation and estimate the signal at every
# sensor position as if the head was still, i.e., in the position measured by the
# initial HPI measurement.
#
# .. tip::
#
#     It is important to first remove the cHPI signal from the recording and to mark
#     bad channels.

raw = filter_chpi(raw)
raw.info["bads"] = [  # strict selection for this example
    "MEG1531",
    "MEG1532",
    "MEG1533",
    "MEG1542",
    "MEG1522",
    "MEG1541",
    "MEG1321",
]
calibration = sample.data_path() / "calibration" / "sss_cal.dat"
cross_talk = sample.data_path() / "cross-talk" / "ct_sparse.fif"
raw_sss = maxwell_filter(
    raw, calibration=calibration, cross_talk=cross_talk, head_pos=head_pos
)

# %%
# Let's visualize the effect on a triplet of sensors located on the top of the head.
# Note however that this represents the effect of SSS and movemvent compensation
# together.

f, ax = plt.subplots(3, 1, sharex=True, figsize=(10, 5), layout="constrained")
times = raw.times[raw.time_as_index(30)[0] :]
picks = ["MEG0711", "MEG0712", "MEG0713"]
for k, pick in enumerate(picks):
    data = raw.get_data(picks=pick, tmin=30).squeeze()
    ax[k].plot(times, data, label="Raw" if k == 0 else None)
    data = raw_sss.get_data(picks=pick, tmin=30).squeeze()
    ax[k].plot(times, data, color="red", label="SSS" if k == 0 else None)
    ax[k].set_title(f"{'MAG:' if k == 0 else 'GRAD:'} {pick}")
plt.show()

# %%
# Magnetometers which are more sensitive to distant fields and thus to environmental
# artifacts are more affected by SSS than gradiometers.
#
# .. note::
#
#     Note that on top of movement compensation, SSS can also transform the signal as if
#     it was emitted from a different head position, through the argument
#     ``destination``. This can be useful to compare signal between subjects in sensor
#     space or to bring back a tilted head to a more upright position.

# %%
# References
# ----------
#
# .. footbibliography::
