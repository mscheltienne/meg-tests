.. include:: ./links.inc

Data analysis PC (DANA)
=======================

A data analysis PC, called DANA, is available in the MEG facility. DANA can be
accessed on the account ``meguser`` and has both MEGIN's analysis software and
MNE-Python.

Specifications
--------------

The analysis PC run on an `intel Xeon W-2245`_ (8 cores, 16 threads) with 32 GB of
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

Like :ref:`meg-settings:Signal Space Projector`\ :footcite:p:`ssp_1997`, SSS is a form
of projection. Whereas SSP empirically determines a noise subspace based on data
(empty-room recordings, EOG or ECG activity, etc) and projects the measurements onto a
subspace orthogonal to the noise, SSS mathematically constructs the external and
internal subspaces from `spherical harmonics`_ and reconstructs the sensor signals using
only the internal subspace (i.e., does an oblique projection).

Introduction taken from `MNE's background on SSS and Maxwell filtering`_.

.. tip::

    Instead of MEGIN's old MaxWell software available on the DANA, the enhanced version
    available in `MNE-Python <mne stable_>`_ is recommended. See
    :func:`mne.preprocessing.maxwell_filter`. The fine calibration file and the
    cross-talk correction are available in the `sample dataset`_ (
    see :func:`meg_wiki.datasets.sample.data_path`).

FIFF format
~~~~~~~~~~~

The FIFF format is MEGIN's proprietary format for MEG data. It is a binary tag based
format. The tags define which information is stored in the file. Thus, the FIFF format
is not restricted to storing the continuous MEG data. For instance, the
:ref:`meg-settings:Signal Space Projector`\ :footcite:p:`ssp_1997` are stored both
in the raw data file and in a separate FIFF file. In both case, the information related
to the SSP is stored in the same FIFF tag.

.. tip::

    `MNE-Python <mne stable_>`_ has command-line tools which can be accessed with:

    .. code-block:: bash

        $ mne <command> <options>

    Entering the command ``$ mne`` will return a list of available commands.

The commands ``mne what`` and ``mne show_fiff`` can be used to inspect the content of
a FIFF file. For instance, to inspect the content of the file
``ssp_68_200123_proj.fif``:

.. code-block:: bash

    $ mne what ssp_68_200123_proj.fif
    proj

.. code-block:: bash

    $ mne show_fiff ssp_68_200123_proj.fif
    999  = FIFFB_ROOT
        100  = FIFF_FILE_ID (20b ids)  = {'version': 65540, 'machid': a ... dict len=4
        101  = FIFF_DIR_POINTER (4b >i4)  = [-1]
        106  = FIFF_FREE_LIST (4b >i4)  = [-1]
        108  = FIFF_NOP (0b nul)
        313  = FIFFB_PROJ
            200  = FIFF_NCHAN (4b >i4)  = [306]
            3002 = FIFF_SPHERE_RADIUS (4b >i4)  = [1]
            3001 = FIFF_SPHERE_ORIGIN (12b >f4)  = [0. 0. 0.] ... array size=3
            314  = FIFFB_PROJ_ITEM
                206  = FIFF_COMMENT/FIFF_DESCRIPTION (24b str)  = ssp_68_magn.fif : PCA-v1 ... str len=24
                3411 = FIFF_PROJ_ITEM_KIND (4b >i4)  = [1]
                3417 = FIFF_PROJ_ITEM_CH_NAME_LIST (2447b str)  = MEG0111:MEG0112:MEG0113:MEG012 ... str len=2447
                3412 = FIFF_PROJ_ITEM_TIME (4b >f4)  = [0.]
                3414 = FIFF_PROJ_ITEM_NVEC (4b >i4)  = [1]
                3415 = FIFF_PROJ_ITEM_VECTORS (1236b >f4)  = [[-0.07794372  0.          0.  ... array size=306
            314  = FIFFB_PROJ_ITEM
                206  = FIFF_COMMENT/FIFF_DESCRIPTION (24b str)  = ssp_68_magn.fif : PCA-v2 ... str len=24
                3411 = FIFF_PROJ_ITEM_KIND (4b >i4)  = [1]
                3417 = FIFF_PROJ_ITEM_CH_NAME_LIST (2447b str)  = MEG0111:MEG0112:MEG0113:MEG012 ... str len=2447
                3412 = FIFF_PROJ_ITEM_TIME (4b >f4)  = [0.]
                3414 = FIFF_PROJ_ITEM_NVEC (4b >i4)  = [1]
                3415 = FIFF_PROJ_ITEM_VECTORS (1236b >f4)  = [[-0.07037429  0.          0.  ... array size=306
            (...)
            314  = FIFFB_PROJ_ITEM
                206  = FIFF_COMMENT/FIFF_DESCRIPTION (24b str)  = ssp_68_grad.fif : PCA-v2 ... str len=24
                3411 = FIFF_PROJ_ITEM_KIND (4b >i4)  = [1]
                3417 = FIFF_PROJ_ITEM_CH_NAME_LIST (2447b str)  = MEG0111:MEG0112:MEG0113:MEG012 ... str len=2447
                3412 = FIFF_PROJ_ITEM_TIME (4b >f4)  = [0.]
                3414 = FIFF_PROJ_ITEM_NVEC (4b >i4)  = [1]
                3415 = FIFF_PROJ_ITEM_VECTORS (1236b >f4)  = [[ 0.00000000e+00  4.50235838e ... array size=306

The tag 314 (``FIFFB_PROJ_ITEM``) contains the information of a single SSP. The tag 3411
(``FIFF_PROJ_ITEM_KIND``) indicates the type of projection. The tag 3417
(``FIFF_PROJ_ITEM_CH_NAME_LIST``) contains the list of channels to which the SSP is
applied.

All MEGIN software work with the FIFF format.

Software
~~~~~~~~

The available software from MEGIN are:

- ``DicomAccess`` is a DICOM v3.0 compliant application for transferring DICOM images.
  The images can be retrieved from a DICOM database or loaded from directories. The
  ``GET`` operation creates FIFF files from the single-frame 16-bit CT, enhanced CT, MR
  and enhanced MR images.
- ``Graph`` is a general purpose signal processor based on a LISP language interpreter.
  This tool is useful to visualize and compared datasets through its different layouts.
- ``GraphicsClipboard`` to generate screenshots of visualizations.
- ``MaxFilter`` to run (temporal) Signal-Space
  Separation\ :footcite:p:`sss_2005,tsss_2006`. See the section about
  :ref:`data-analysis-pc:MaxWell filter`.
- ``MEG-MRI-Integration``, also called ``mrilabl``, is a tool to visualize volumetric
  data. It's especially designed to combine MRI and MEG data.
- ``MRI-segmentation``, also called ``seglab``, is a segmentation program with both 2D
  processing operators (for single images) and 3D processing operators (for volume
  data).
- ``Plotting``, also called ``xplotter``, is a plotting tool mainly intended for
  plotting of evoked response data.
- ``SourceModelling``, also called ``xfit``, for dipole fitting.
- ``ViewBrain`` is used to visualize volumetric data. It can render segmented MRI as 3D
  images and overlay Equivalent Current Dipoles (ECDs).

Python
------

MNE-Python
----------

FreeSurfer
----------

MATLAB
------

The data analysis PC does not have a MATLAB license. However, applications using the
MATLAB Runtime can be added upon request.

References
----------

.. footbibliography::
