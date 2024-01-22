.. include:: ../links.inc

Electrophysiology
=================

Electroencaphalography (EEG)
----------------------------

The MEG system can simultaneously record MEG and EEG data. The EEG amplifiers support
up to 128 channels split on 4 LEMO connectors (32 channels per connector). The ground
and the reference are connected on 2 separate touchproof connectors and require 2 MEG
compliant touchproof leads. On the platform, the following caps are available:

+--------+---------------------------+---------------------------+----------------------------+
|        | .. centered:: 32 channels | .. centered:: 64 channels | .. centered:: 128 channels |
+--------+---------------------------+---------------------------+----------------------------+
| Small  |                           | .. centered:: X           |                            |
+--------+---------------------------+---------------------------+----------------------------+
| Medium |                           | .. centered:: X           | .. centered:: X            |
+--------+---------------------------+---------------------------+----------------------------+
| Large  |                           | .. centered:: X           | .. centered:: X            |
+--------+---------------------------+---------------------------+----------------------------+

The EEG electrodes can be digitized are part of the
:ref:`digitization <meg-session:Digitization>` process using the
`Polhemus FASTRAK system <Polhemus_>`_. The digitized EEG electrodes can be used to (1)
improve scalp topographies of EEG signal with "True" electrode locations, (2) improve
the co-registration through additional digitization points on the scalp surface.

BIO channels
------------

The MEG system can record from 12 bipolar channels, also called ``BIO`` channels. The
``BIO`` channels can be set to record EOG, ECG, EMG, or any other bipolar montage.

.. note::

    MEGIN and its FIFF format can store the channel type information for EOG, ECG and
    EMG channels. To do so, in the
    :ref:`channel selection <meg-settings:Channel selection>` panel, click on
    ``Edit BIO``.

MEG compliant touchproof leads
------------------------------

MEG sensitivity to external magnetic fields prevent the use of most metal-based leads.
Breathing, heart beat, and any other movement of the subject will slightly move the
leads which will generate noise on the MEG sensors.

To avoid this problem, the leads used on the MEG platform are derived from the
`LEAD108C`_ for MRI systems. The leads are made of plastic with a carbon-fiber leadwire
and a carbon filled ABS plastic clip. The leads are 1.8 meters long.
