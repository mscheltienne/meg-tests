MEG session
===========

Screening
---------

An MEG session starts by screening the participant to ensure his compatibility with
MEG acquisition (see :ref:`meg-contraindications:MEG contraindications`). An MEG
measures fields in the range of :math:`fT`, i.e. :math:`e^{-15}\ Tesla`. Thus, it's very
sensitive to any magnetic metal or alloy in movement within the Magnetically Shielded
Room (MSR). For instance, the ticking of the second's needle of a mechanical watch is
picked up 2 meters from the sensors.

During screening, the participant is positioned in the MEG and the signal is monitored
for a short period of time. Screening is an iterative process where we try to identify
and remove all sources of interference. Common sources of interference are: braces,
dental retainers, piercings, make-up, bra, .. see
:ref:`meg-contraindications:MEG contraindications` for an exhaustive list.

.. note::

    Participants will change into MEG-compatible clothes thus removing belts, jeans,
    bras and other clothes with metallic pieces.

If the interference source can not be removed, e.g. implants or dental retainers, the
decision to continue or cancel the acquisition belongs to the researcher. In practice,
we recommend to exclude participants which do not yield clean signal, except if they are
part of a rare cohort. In theory, :ref:`MaxWell filtering and Spatiotemporal SSS (tSSS)
<data-analysis-pc:MaxWell filter>` can remove most noise components.

Empty-Room recording
--------------------

Before the experiment begins, an empty-room recording is measured. The empty-room
recording can be used to :ref:`re-compute the Signal Space Projectors (SSP)
<tut-artifact-ssp>`.

The default Signal Space Projectors have been tuned for our site and the empty-room
noise present. This noise and its correction are stable in time, thus it should not
be needed to re-compute the SSPs. However, the empty-room recording can be used to
compare the SSP correction with the empty-room noise correction from the ``08/01/24``.
On that day, the bad sensors removed are ``MEG 1213``, ``MEG 1321``, ``MEG 1343``,
``MEG 1423``.

.. code-block:: python

    from matplotlib import pyplot as plt
    from mne.io import read_raw_fif

    fname = r"empty_room_raw.fif"
    raw = read_raw_fif(fname, preload=True).apply_proj()
    fig = raw.compute_psd().plot(show=False)
    fig.axes[0].set(xlim=(0, 50), ylim=(5, 40))
    fig.axes[1].set(xlim=(0, 50), ylim=(5, 40))
    plt.show()

.. tab-set::

    .. tab-item:: Position 68°

        .. image:: ./_static/ssp/psd-68deg-dark.svg
            :class: only-dark
            :align: center
            :width: 700

        .. image:: ./_static/ssp/psd-68deg-light.svg
            :class: only-light
            :align: center
            :width: 700

    .. tab-item:: Position 60°

        .. image:: ./_static/ssp/psd-60deg-dark.svg
            :class: only-dark
            :align: center
            :width: 700

        .. image:: ./_static/ssp/psd-60deg-light.svg
            :class: only-light
            :align: center
            :width: 700

    .. tab-item:: Position 0°

        .. image:: ./_static/ssp/psd-0deg-dark.svg
            :class: only-dark
            :align: center
            :width: 700

        .. image:: ./_static/ssp/psd-0deg-light.svg
            :class: only-light
            :align: center
            :width: 700

Digitization
------------

Contrary to EEG, the head and the sensors are not in the same coordinate frame. In other
words, the sensors are fixed and the participant is free to position his head within the
helmet in different ways and to move during the recording. Thus, for 2 different
participants or 2 different recording sessions, the head position inside the MEG helmet
might vary. In other words, a given sensor will not monitor the same brain region.

To account for the variable head position, a device to head transformation is estimated
for every recording. This transformation is estimated from 5 ciols placed on the
participant head. The coils position is measured both in the head coordinate frame (as
part of the digitization process) and in the device coordinate frame (as part of the
HPI measurement).

.. image:: ./_static/coordinate-frame/head-coordinate-frame.png
    :align: right
    :width: 200

The digitization process is performed with the `Polhemus FASTRAK system <Polhemus_>`_.
First, 3 landmarks are digitized: the `nasion (NAS) <Nasion_>`_, the `left and right
pre-auricular point (LPA and RPA) <LRPA_>`_. Those 3 landmarks define the head
coordinate frame:

- The X-axis goes from `LPA (2) to RPA (1) <LRPA_>`_
- The Y-axis is orthogonal to the X-axis and goes through the
  `nasion (NAS) <Nasion_>`_ (3)
- The Z-axis forms the right-handed orthogonal system

The head coordinate frame measures the point's position in meters.

TODO: Add picture of the Nasion/LPA/RPA points used on our site.

HPI measurement
---------------

Experiment
----------

.. _LRPA: https://www.fieldtriptoolbox.org/faq/how_are_the_lpa_and_rpa_points_defined/
.. _Nasion: https://en.wikipedia.org/wiki/Nasion
.. _Polhemus: https://polhemus.com/motion-tracking/all-trackers/fastrak/
