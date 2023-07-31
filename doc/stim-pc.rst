Stimulation PC
==============

The stimulation PC is connected to the :ref:`stim-devices/index:Stimulation devices`. It
can boot on Windows 10 or on Ubuntu 22.04 LTS (generic or lowlatency kernel). In both
case, users should use the non-admin account ``meguser``.

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

        TODO

    .. tab-item:: Python (Linux)

        TODO

    .. tab-item:: MATLAB (Windows)

        TODO

.. _Chronos: https://pstnet.com/products/chronos/
.. _intel i5-12500: https://ark.intel.com/content/www/us/en/ark/products/96144/intel-core-i512500-processor-18m-cache-up-to-4-60-ghz.html
.. _Nvidia T1000: https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/productspage/quadro/quadro-desktop/proviz-print-nvidia-T1000-datasheet-us-nvidia-1670054-r4-web.pdf
