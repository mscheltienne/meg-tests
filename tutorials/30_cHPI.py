r"""
.. _tut-cHPI:

Correct head movements with cHPI
================================

.. include:: ../../links.inc

.. note::

    This example requires the ``meg_wiki`` package to download the sample dataset. This
    package can be installed with ``pip``:

    .. code-block:: bash

        $ pip install git+https://github.com/fcbg-hnp-meeg/meg-wiki

:ref:`Signal-Space Separation (SSS) and Maxwell filter
<data-analysis-pc:MaxWell filter>`\ :footcite:p:`sss_2005,tsss_2006` can be used to
compensate for head movements during a recording. To run SSS, you can use either MEGIN's
software on the :ref:`DANA <data-analysis-pc:MEGIN's software>` or
`MNE-Python <mne stable_>`_'s implementation.

.. note::

    The enhanced version available in `MNE-Python <mne stable_>`_ is recommended. See
    :func:`mne.preprocessing.maxwell_filter`. The fine calibration file and the
    cross-talk correction are available in the `sample dataset`_ (
    see :func:`meg_wiki.datasets.sample.data_path`).
"""

from pathlib import Path

from mne.datasets import fetch_fsaverage
from mne.io import read_raw_fif
from mne.viz import plot_alignment, set_3d_view

from meg_wiki.datasets import sample

# %%
# Head Position Indicator (HPI)
# -----------------------------
#
# :ref:`Head Position Indication (HPI) <meg-session:HPI measurement>` is a technique to
# measure the head position with respect to the MEG sensors. 5 coils are placed on the
# participant head and digitized (see this
# :ref:`section about digitization <meg-session:Digitization>`) in the head coordinate
# frame. At the beginning of a recording, an electromagnetic pulse if delivered on the 5
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
