DACQ settings
=============

DACQ settings can be changed in the configuration file
``/neuro/dacq/setup/megacq.defs``. You can edit the configuration file with:

.. code-block:: bash

    $ sudo nano /neuro/dacq/setup/megacq.defs

Speed-up phantom acquisition
----------------------------

Reset between pulses
~~~~~~~~~~~~~~~~~~~~

To speed-up the phantom acquisition, we can change the time we wait after a channel
reset. This will likely reduce the quality of the first epochs per dipole, but they will
be rejected by the fitting tool.

.. code-block:: bash

    $ cat /neuro/dacq/setup/megacq.defs | grep phantom

The setting to change is ``DEFphantomWaitAfterReset`` which defaults to 3000 ms.

.. note::

    With this version of the electronics, we can set this value to -1 which will disable
    the reset between dipoles entirely.

Number of repetition
~~~~~~~~~~~~~~~~~~~~

The number of repetition per dipole can be changed in the phantom setup.

.. code-block:: bash

    $ cat /neuro/dacq/setup/phantom/phantom.set | grep Nave

The number of repetition is controlled independently for each dipole and defaults to
100.
