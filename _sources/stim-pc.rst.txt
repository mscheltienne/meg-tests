.. include:: ./links.inc

Stimulation PC
==============

The stimulation PC is connected to the stimulation devices. It can boot on Windows
10 or on Ubuntu 22.04 LTS (generic or lowlatency kernel). In both case, users should use
the non-admin account ``meguser`` and projects should be stored in ``~/projects``.

Specifications
--------------

The stimulation PC runs on an `intel Xeon W-2245`_ (8 cores, 16 threads) with 32 GB of
RAM and an `Nvidia Quadro P2200`_. This hardware is recent but not high-end. Stimulation
paradigms rarely require high-end hardware with high throughput. Instead, latency and
regularity are more valuable and are similar between high-end and middle-end
hardware.

E-Prime
-------

E-Prime is designed to work with a `Chronos`_ device to manage both auditory outputs and
I/O lines, among which triggers. If the `Chronos`_ is not used, the settings should be
set to:

- parallel port to ``LPT4``
- audio driver to ``ASIO``

.. warning::

    With audio stimulation, the ``DirectSound`` driver yields unreliable timings.

Finally, the monitor index should be set to ``1`` or ``2``, but E-Prime does not
identify the monitor index reliably and might swap the monitor index between 2 reboots.

Python
------

For Python, virtual environments are used to separate the dependencies of different
projects and paradigms. The virtual environment can be created either through VSCode or
through a terminal. The python version defined in the `SPEC 0`_ by the scientific python
community are available on the stimulation PC, as of writing, python 3.9 to python 3.12.

.. important::

    The stimulation PC prevents ``pip`` installation of packages within the base
    environment.

.. tab-set::

    .. tab-item:: VSCode

        In VSCode, open the folder from your project, e.g. ``~/projects/my_project``.
        Using the command palette (``Ctrl+Shift+P``), search for
        ``Python: Select Interpreter``. You can then create an environment using
        ``venv`` and the python interpreter (version) of your choice.

        The created virtual environment will be placed in the current directory in the
        folder ``.venv``, i.e. ``~/projects/my_project/.venv``. Subsequent terminals
        opened in VSCode while this folder is opened will automatically activate the
        virtual environment.

        You can now install packages in this virtual environment with ``pip``:

        .. code-block:: bash

            $ pip install numpy

        This method works both for Windows and Linux.

    .. tab-item:: Windows

        In a command prompt or terminal (recommended: ``Cmder``), navigate to the
        project location and to the folder in which you wish to create the virtual
        environment. You can create the virtual environment with ``venv``:

        .. code-block:: bash

            $ py -m venv .venv

        .. note::

            You can replace ``.venv`` with the name of the environment. This name will
            be used to create the folder in which the environment will be stored.

        .. note::

            If you wish to select a different python version than the version bind to
            ``py``, specify the version after ``py``. For instance the command below
            launches a 3.11 python interpreter (if installed on the system).

            .. code-block:: bash

                $ py -3.11

        Once created, you can activate the environment with:

        .. code-block:: bash

            $ .venv\Scripts\activate.bat

        .. note::

            You will always have to manually activate the environment in new terminals.

        You can now install packages in this virtual environment with ``pip``:

        .. code-block:: bash

            $ pip install numpy

    .. tab-item:: Linux

        In a terminal, navigate to the project location and to the folder in which you
        wish to create the virtual environment. You can create the virtual environment
        with ``venv``:

        .. code-block:: bash

            $ python3.10 -m venv .venv --copies

        .. note::

            You can replace ``.venv`` with the name of the environment. This name will
            be used to create the folder in which the environment will be stored.

        .. note::

            If you wish to select a different python version, replace ``python3.10``
            with, the appropriate version. For instance, the command below launches a
            3.12 python interpreter.

            .. code-block:: bash

                $ python3.12

        You can now install packages in this virtual environment with ``pip``:

        .. code-block:: bash

            $ pip install numpy

PsychoPy
--------

A default PsychoPy ``2023.2.3`` installation is available on the Windows partition.
However, it is recommended to use a virtual environment to install the latest version of
PsychoPy when able.

MATLAB
------

MATLAB ``R2024a`` is installed on both the Windows and Linux partition of the
stimulation PC.

.. tab-set::

    .. tab-item:: Windows

        On Windows, a shortcut on the desktops are available. Psychtoolbox version
        ``3.0.19.13`` is installed.

    .. tab-item:: Linux

        On Linux, the executable is located here: ``/usr/local/bin/matlab``.

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

            :class:`~byte_triggers.ParallelPortTrigger` automatically resets the
            parallel port to ``0`` after each trigger, in a separate thread. This avoids
            blocking the main thread. The default reset delay is set to ``10 ms``.

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

            :class:`~byte_triggers.ParallelPortTrigger` automatically resets the
            parallel port to ``0`` after each trigger, in a separate thread. This avoids
            blocking the main thread. The default reset delay is set to ``10 ms``.

    .. tab-item:: MATLAB (Windows)

        1. Download :download:`io64.mexw64 <./_static/downloads/triggers/io64.mexw64>`
           in your MATLAB path
        2. In MATLAB, use the following code to send triggers between ``1`` and ``255``:

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

        .. note::

            If you need precise control on the monitor refresh rate, make sure that the
            wait delay is smaller than the interval between 2 frames. On the stimulation
            PC, the :ref:`ProPixx projector <devices/visual:ProPixx projector>` has a
            120 refresh rate, i.e. 2 frames are separated y 8.33 ms.

Measuring trigger to event delay
--------------------------------

Delays between an :ref:`MEG trigger <meg-triggers:MEG triggers>` and an event can be
measured by connecting a measuring device to a miscellaneous channel of the MEG system.
The :ref:`sampling rate <meg-settings:Sampling rate>` can be increased to 5 kHz to
measure higher frequency content.

For **visual task**, a photodiode is available. The photodiode optical fiber should be
connected to the powered digitizer. The analogical output of the digitizer is sufficient
in most cases, and should be preferred above the thresholded digital output.

For **auditory task**, one of the monitoring output from the `Crimson 3`_, ``Phones 1``
can be connected via a jack to BNC cable to a miscellaneous channel, ``MISC 006``. See
additional information about this measure in the
:ref:`trigger to sound onset delay <devices/audio/index:Trigger to sound onset delay>`
section and in the tutorial :ref:`tut-proxy-audio-measure`.

Ethernet TCP/UDP
----------------

The stimulation PC has an extra GigE network card, `TP-Link TG-3468`_, which can be used
in paradigms for network based communications.
