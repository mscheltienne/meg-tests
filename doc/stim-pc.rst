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

.. _intel i5-12500: https://ark.intel.com/content/www/us/en/ark/products/96144/intel-core-i512500-processor-18m-cache-up-to-4-60-ghz.html
.. _Nvidia T1000: https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/productspage/quadro/quadro-desktop/proviz-print-nvidia-T1000-datasheet-us-nvidia-1670054-r4-web.pdf
