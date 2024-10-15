DACQ settings
=============

DACQ settings can be changed in the configuration file
``/neuro/dacq/setup/megacq.defs``.

Speed-up phantom acquisition
----------------------------

Reset between pulses
~~~~~~~~~~~~~~~~~~~~

To speed-up the phantom acquisition, we can change the reset time between dipole
pulses.

.. code-block:: bash

    $ cat /neuro/dacq/setup/megacq.defs | grep phantom
    $ sudo nano /neuro/dacq/setup/megacq.defs

The setting to change is ``DEFphantomWaitAfterReset`` which defaults to 3000 ms.

Number of repetition
~~~~~~~~~~~~~~~~~~~~

The number of repetition per dipole can be changed in the phantom setup.

.. code-block:: bash

    $ cat /neuro/dacq/setup/phantom/phantom.set | grep Nave

The number of repetition is controlled independently for each dipole and defaults to
100.
