.. include:: ./links.inc

Stimulation PC
==============

The stimulation PC is connected to the
:ref:`stimulation devices <devices/index:Stimulation devices>`. It can boot on Windows
10 or on Ubuntu 22.04 LTS (generic or lowlatency kernel). In both case, users should use
the non-admin account ``meguser``.

Specifications
--------------

The stimulation PC runs on an `intel i5-12500`_ (6 cores, 12 threads) with 16 GB of RAM
and an `Nvidia T1000`_. This hardware is recent but not high-end. Stimulation
paradigms rarely require high-end hardware with high throughput. Instead, latency and
regularity are more valuable and are similar between high-end and middle-end
hardware.

E-Prime
-------

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

            trigger = ParallelPortTrigger(0x4FB8)  # hexadecimal address
            trigger.signal(101)

        .. note::

            The :class:`~byte_triggers.ParallelPortTrigger` automatically resets the
            parallel port to ``0`` after each trigger, in a separate thread. This avoids
            blocking the main thread. The default reset delay is set to ``50 ms``.

        .. note::

            Note that the :ref:`stimulation PC <stim-pc:Stimulation PC>` is
            pre-configured. On other computers, microsoft redistributables and the
            :download:`inpoutx64.dll <./_static/triggers/inpoutx64.dll>` file in
            ``C:\Windows\system32`` may be required.

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

        1. Download :download:`io64.mexw64 <./_static/triggers/io64.mexw64>` in your
           MATLAB path
        2. In MATLAB, use the following code to send triggers betwwn ``1`` and ``255``:

        .. code-block:: matlab

            %% Initialize the parallel port object
            address = hex2dec("4FB8");
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
            :download:`inpoutx64.dll <./_static/triggers/inpoutx64.dll>` file in
            ``C:\Windows\system32`` may be required.
