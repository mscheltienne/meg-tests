.. include:: ../../links.inc

Fine calibration and SSS shielding actor
========================================

The fine calibration file is provided in the ``sss_cal.dat`` file and is used by the
:ref:`data-analysis-pc:MaxWell filter` software. The fine calibration improves by a
factor of 10 or 100 the "SSS shielding factor", i.e. how well SSS removes artifacts from
the signal.

.. note::

    In MNE-Python's implementation of :func:`mne.preprocessing.maxwell_filter`, the fine
    calibration file is provided in the argument ``calibration``.

The "default" fine calibration file in the sample dataset:

.. code-block:: Python

    from mne_wiki.datasets import sample

    fine_cal_file = sample.data_path() / "calibration" / "sss_cal.dat"

This default fine calibration file is computed during the annual maintenance of the MEG
and is stable over time. However, it can also be re-computed from an empty-room
recoridng.

Computing the fine calibration
------------------------------

MNE-Python provides the function :func:`mne.preprocessing.compute_fine_calibration` to
compute the fine calibration from empty-room data.

.. note::

    MNE-Python's docstring mentions that all channels should be good, probably because
    of the channel selection occurring under-the-hood and to the creation of an output
    structure which *has* to include all channels. However, it seems that bad or noisy
    channels have little effect on the fine calibration. Thus, MNE-Python's docstring
    can be understood as "do not mark bad channels as bad, just let the function handle
    them".

The service tools also include scripts to compute the fine calibration and the SSS
shielding factor.

.. code-block:: bash

    $ /neuro/dacq/tools/bin/meg_calib -v -f empty_room_68.fif

SSS shielding factor
--------------------

``xfilter`` can estimate the SSS shielding factor with (1) default fine calibration and
(2) a custom fine calibration file.

.. code-block:: bash

    $ /neuro/dacq/tools/bin/xfilter -v -f empty_room_68.fif -sf
    $ /neuro/dacq/tools/bin/xfilter -v -f empty_room_68.fif -sf -cal sss_cal.dat

You can then compare the ``*.xfilter.txt`` reports, e.g. with:

.. code-block:: bash

    $ more *.xfilter.txt
