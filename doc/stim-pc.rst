.. include:: ./links.inc

Stimulation PC
==============

The stimulation PC is connected to the
:ref:`stimulation devices <devices/index:Stimulation devices>`. It can boot on Windows
10 or on Ubuntu 22.04 LTS (generic or lowlatency kernel). In both case, users should use
the non-admin account ``meguser``.

Specifications
--------------

The stimulation PC runs on an `intel Xeon W-2245`_ (8 cores, 16 threads) with 32 GB of
RAM and an `Nvidia Quadro P2200`_. This hardware is recent but not high-end. Stimulation
paradigms rarely require high-end hardware with high throughput. Instead, latency and
regularity are more valuable and are similar between high-end and middle-end
hardware.

E-Prime
-------

In E-Prime, if the `Chronos`_ is not used, the settings should be set to:

- the monitor should be set to ``1``
- the parallel port to ``LPT4``
- the audio driver to ``ASIO``

.. warning::

    With audio stimulation, the ``DirectSound`` driver yields unreliable timings.

Python
------

.. tab-set::

    .. tab-item:: Windows

        TODO

    .. tab-item:: Linux

        TODO

PsychoPy
--------

.. tab-set::

    .. tab-item:: Windows

        TODO

    .. tab-item:: Linux

        TODO

MATLAB
------

Triggers
--------

The stimulation PC can send triggers to the first 8 bits of the trigger interface on the
main desk, ``STI102``, via a parallel port (DB-25) or via the `Chronos`_ if
:ref:`stim-pc:E-Prime` is in-use. The triggers should last a couple of millisecond, 10
ms is recommended. The parallel port should be initialized to ``0`` at the beginning of
the paradigm and it should be reset to ``0`` after each trigger.

.. tab-set::

    .. tab-item:: Python (Windows)

        The platform provides `byte-triggers`_ to send triggers in paradigm. It supports
        :class:`~byte_triggers.MockTrigger` (for testing purposes),
        :class:`~byte_triggers.LSLTrigger` (for software triggers) and
        :class:`~byte_triggers.ParallelPortTrigger` (for hardware triggers).

        .. code-block:: python

            from byte_triggers import ParallelPortTrigger

            trigger = ParallelPortTrigger(0x2FB8)  # hexadecimal address
            trigger.signal(101)

        .. note::

            The :class:`~byte_triggers.ParallelPortTrigger` automatically resets the
            parallel port to ``0`` after each trigger, in a separate thread. This avoids
            blocking the main thread. The default reset delay is set to ``50 ms``.

        .. note::

            Note that the :ref:`stimulation PC <stim-pc:Stimulation PC>` is
            pre-configured. On other computers, microsoft redistributables and the
            :download:`inpoutx64.dll <./_static/downloads/triggers/inpoutx64.dll>` file
            in ``C:\Windows\system32`` may be required.

    .. tab-item:: Python (Linux)

        The platform provides `byte-triggers`_ to send triggers in paradigm. It supports
        :class:`~byte_triggers.MockTrigger` (for testing purposes),
        :class:`~byte_triggers.LSLTrigger` (for software triggers) and
        :class:`~byte_triggers.ParallelPortTrigger` (for hardware triggers).

        .. code-block:: python

            from byte_triggers import ParallelPortTrigger

            trigger = ParallelPortTrigger("/dev/parport0")
            trigger.signal(101)

        .. note::

            The :class:`~byte_triggers.ParallelPortTrigger` automatically resets the
            parallel port to ``0`` after each trigger, in a separate thread. This avoids
            blocking the main thread. The default reset delay is set to ``50 ms``.

    .. tab-item:: MATLAB (Windows)

        1. Download :download:`io64.mexw64 <./_static/downloads/triggers/io64.mexw64>`
           in your MATLAB path
        2. In MATLAB, use the following code to send triggers betwwn ``1`` and ``255``:

        .. code-block:: matlab

            %% Initialize the parallel port object
            address = hex2dec("2FB8");
            ioObj = io64;
            status = io64(ioObj);
            io64(ioObj, address, 0);  % set the parallel port to 0 (default state)

            %% Deliver the trigger 101
            io64(ioObj, address, 101);  % set the parallel port to 101
            pause(0.01);  % wait for 10 ms
            io64(ioObj, address, 0);  % set the parallel port back to 0

        .. note::

            Note that the :ref:`stimulation PC <stim-pc:Stimulation PC>` is
            pre-configured. On other computers, microsoft redistributables and the
            :download:`inpoutx64.dll <./_static/downloads/triggers/inpoutx64.dll>` file
            in ``C:\Windows\system32`` may be required.

Measuring timings
-----------------

Timings can be measured by connecting a measuring device to a miscellaneous channel of
the MEG system. The :ref:`sampling rate <meg-settings:Sampling rate>` can be increased
to 5 kHz to measure higher frequency content.

For visual task, a photodiode is available. The photodiode optical fiber should be
connected to the powered digitizer. The analogical output of the digitizer is sufficient
in most cases, and should be preferred above the thresholded digital output.

For auditory task:

- one of the monitoring output from the `Crimson 3`_ can be connected via a jack to BNC
  cable to a miscellaneous channel.
- the :ref:`optimic <devices/optimic:Optimic>` can be used to record the sound output
  from the headset.

This testing setup works best with a pure tone sound at 1 kHz, downloadable below:

.. image:: ./_static/icons/audio-file.svg
    :align: center
    :alt: Download sound file
    :target: ./_static/downloads/sound/tone_1000Hz.wav
    :width: 100
