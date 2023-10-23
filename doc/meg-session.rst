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
dental retainers, piercings, make-up, bra.

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

Experiment
----------
