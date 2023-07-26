MEG triggers
============

The MEG system has 32 binary channels that can be used for triggers. Those 32 channels
are split between 2 trigger interface I/O boxes, one on the main desk connected to
the :ref:`stim-pc:Stimulation PC` and one in the stimulus cabinet.

.. image:: ./_static/meg/meg-triggers.png
    :width: 700
    :align: center

Binary vs combined channel
--------------------------

The channels ``STI01``, ``STI02``, ..., ``STI16`` are binary channels. They measure a
single TTL pulse which drives the channel from 0 to 1 and vice versa.
The channels ``STI101`` and ``STI102`` are combined channels which measure the 16
binary channels associated to their respective trigger interface I/O box at once. The
value measured by a combined channel corresponds to the decimal value of the binary
number expressed on the binary channels. For instance, if the channels 1, 3, 4 of the
trigger interface I/O box in the stimulus cabinet receive a pulse, the combined channel
``STI101`` receives the decimal value which corresponds to the binary number ``1101``
(from left to right, channel 4 is high, channel 3 is high, channel 2 is low and channel
1 is high). In decimal, this number equals 13.

Thus, if 8 BNC cables are connected, e.g., from the computer DB-25 port (parallel port),
the combined channel can receives triggers ranging from 0 to 255 (8 bits unsigned
integer). In theory, with 16 channels each, combined channels can measure trigger
ranging from 0 to 65535.

STI101 and STI102
-----------------

```STI101`` and ``STI102`` are the names of the 2 combined channels corresponding to
each trigger interface I/O box. ``STI101`` corresponds to the one in the stimulus
cabinet and ``STI102`` to the one on the main desk. By default, both trigger interface
I/O box work in *synchronous* mode. In this mode, you effectively have only 16 binary
channels, mirrored between both boxes. In other words, if a trigger arrives on the
channel 1 of the box in the stimulus cabinet, the same trigger will be received on the
channel 1 of the box on the main desk.

To desynchronize the trigger interface I/O boxes, the channel ``STI102`` must be
enabled. When desynchronized, a trigger which arrives on the channel 1 of the box in the
stimulus cabinet is not mirrored on the channel 1 of the box on the main desk.

.. note::

    This channel is disabled by default and it is not possible to change the default.
