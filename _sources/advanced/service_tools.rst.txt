Service tools
=============

The DACQ contains many useful service tools that can help in the daily MEG activity.

autonoises
----------

The ``autonoises`` tool is used to measure the noise level in the MEG room and to
auto-detect noisy or out of range channels. This tool runs on an empty-room recording.

.. code-block:: bash

    $ /neuro/dacq/tools/noise/autonoises emptyroom_68.fif

dossp
-----

The ``dossp`` tool is used to compute SSP projectors from an empty-room recording.
The tool will:

- Select a channel type
- Apply filters (by default, low-pass @ 48 Hz)

  .. note::

      The filters do not retain the line frequency noise on purpose. Line frequency is
      rarely corrected by SSPs projector.

  .. note::

      It might be better to remove the DC component with an (0.1, 48) Hz bandpass
      filter.

- Compute the covariance matrix
- Compute the PCA decomposition of the covariance matrix and keep the first N components
  (8 by default)
- Removes components which are locked on a sensor

.. code-block:: bash

    $ /neuro/dacq/tools/noise/dossp emptyroom_68.fif

.. note::

    The filters parameters differ from MNE's default which yields differences in the
    obtained projectors between ``dossp`` and MNE's function
    :func:`~mne.compute_proj_raw`. Moreover, our site has a strong 16.7 hz noise coming
    from the railway electrificatin system. This artifact can be very well captured by
    1-3 components estimated on the narrowband 15-18 Hz. The projectors from the
    narrow and wideband PCA can be combined to form an orthogonal basis.

autophantom
-----------

Autophantom automatically fits the measured dipoles with ``xfit`` and compares it with
the known true position of each individual dipole. It requires an evoked (average) FIFF
file as input.

.. code-block:: bash

    $ /neuro/dacq/tools/service/autophantom phantom_avg.fif --pdf
