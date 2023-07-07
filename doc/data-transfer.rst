Data transfer (Isilon)
======================

A network share, Isilon, is available on FCBG's facilities. This network share can be
accessed from one of 3 networks: FCBG (``campusbiotech.ch``), EPFL (``epfl.ch``) and
UNIGE (``unige.ch``). Each lab has a separate share with lab-wide credentials and can
mount the share on their computer using those credentials.

The data acquisition PC (DACQ) has accessed to the shares from labs using the MEG
facility, and recordings can be transferred to their owner via this network share.

.. note::

    Isilon is a **temporary** storage location. The goal is to transfer data from our
    facilities to the users. The shares should be regularly clean-up by the users.
    Old datasets can be removed from both the DACQ and Isilon without prior notice.
    Neither the DACQ or Isilon is meant to store a backup of the recordings.

Request Isilon credentials
--------------------------

If you confirmed with your lab members that you do not already possessed an Isilon share
and account, you can contact FCBG's IT service at helpdesk@fcbg.ch to create one.

Mount Isilon network shares
---------------------------

Isilon uses samba to manage the network share. The address depends on the organization
you belong to (and thus on the network you are connected to) and on the share name.

.. tab-set::

    .. tab-item:: FCBG

        If you are connected to the FCBG network, e.g., if you are using the
        :ref:`stim-pc:Stimulation PC` or the
        :ref:`data-analysis-pc:Data analysis PC (DANA)`, the domain is
        ``campusbiotech.ch``. For example, for the share ``0000_CBT_EPFL_XXXXXX``, the
        address is:

        .. code-block:: bash

            fcbgnas.campusbiotech.ch/fcbgdata/0000_CBT_EPFL_XXXXXX

    .. tab-item:: EPFL

        If you are connected to the EPFL network, the domain is ``epfl.ch``. For
        example, for the share ``0000_CBT_EPFL_XXXXXX``, the address is:

        .. code-block:: bash

            fcbgnas.epfl.ch/fcbgdata/0000_CBT_EPFL_XXXXXX

    .. tab-item:: UniGE

        If you are connected to the UniGE network, the domain is ``unige.ch``. For
        example, for the share ``0000_CBT_EPFL_XXXXXX``, the address is:

        .. code-block:: bash

            fcbgnas.unige.ch/fcbgdata/0000_CBT_EPFL_XXXXXX

Once the address and credentials are known, mounting the network share differs depending
on the OS.

.. note::

    On the ``meguser`` account of the :ref:`stim-pc:Stimulation PC` and
    :ref:`data-analysis-pc:Data analysis PC (DANA)`, you can find a PDF describing the
    mounting procedure on the desktop.
