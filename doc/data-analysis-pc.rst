Data analysis PC (DANA)
=======================

Data analysis PCs, called DANA, are available in the MEG facility. DANA's can be
accessed on the account ``meguser`` and have both MEGIN's analysis software and
MNE-Python.

Specifications
--------------

The stimulation PC runs on an `intel Xeon W-2245`_ (8 cores, 16 threads) with 32 GB of
RAM and an `Nvidia Quadro P2200`_. Most analysis pipeline require one or multiple copies
of a dataset to be loaded in RAM. 32 GB is sufficient for subject-level analysis and
most group-level analysis, with an additional 20 GB of available swap if needed.

MEGIN's software
----------------

MaxWell filter
~~~~~~~~~~~~~~

Signal-Space Separation (SSS)\ :footcite:p:`sss_2005,tsss_2006` is a technique based on
the physics of electromagnetics fields. SSS separates the measured signal into
components attributable to sources inside the measurement volume of the sensor array
(the internal components), and components attributable to sources outside the
measurement volume (the external components). The internal and external components are
linearly independent, so it is possible to simply discard the external components to
reduce environmental noise.

Maxwell filtering is a related procedure that omits the higher-order components of the
internal subspace, which are dominated by sensor noise. Typically, Maxwell filtering and
SSS are performed together.

Like Signal-Space Projection (SSP), SSS is a form of projection. Whereas SSP empirically
determines a noise subspace based on data (empty-room recordings, EOG or ECG activity,
etc) and projects the measurements onto a subspace orthogonal to the noise, SSS
mathematically constructs the external and internal subspaces from
`spherical harmonics`_ and reconstructs the sensor signals using only the internal
subspace (i.e., does an oblique projection).

Introduction taken from `MNE-Python's background on SSS and Maxwell filtering`_.

Python
------

MNE-Python
----------

FreeSurfer
----------

MATLAB
------

The data analysis PCs do not have a MATLAB license. However, applications using the
MATLAB Runtime can be added upon request.

.. _intel Xeon W-2245: https://www.intel.com/content/www/us/en/products/sku/198609/intel-xeon-w2245-processor-16-5m-cache-3-90-ghz/specifications.html
.. _Nvidia Quadro P2200: https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/quadro-p2200-datasheet-letter-974207-r4-web.pdf
.. _spherical harmonics: https://en.wikipedia.org/wiki/Spherical_harmonics
.. _MNE-Python's background on SSS and Maxwell filtering: https://mne.tools/stable/auto_tutorials/preprocessing/60_maxwell_filtering_sss.html#background-on-sss-and-maxwell-filtering

References
----------

.. footbibliography::
