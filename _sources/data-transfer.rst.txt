Data transfer (Isilon)
======================

A network share, Isilon, is available on FCBG's facilities. This network share can be
accessed from one of 3 networks: FCBG (``campusbiotech.ch``), EPFL (``epfl.ch``) and
UNIGE (``unige.ch``). Each lab has a separate share with lab-wide credentials and can
mount the share on their computer using those credentials.

The data acquisition PC (DACQ) has access to the shares from labs using the MEG faciliy,
and recordings can be transferred to their owner via this network share.

.. important::

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
        :ref:`stimulation PC <stim-pc:Stimulation PC>` or the
        :ref:`data analysis PC <data-analysis-pc:Data analysis PC (DANA)>`, the domain
        is ``campusbiotech.ch``. For example, for the share ``0000_CBT_EPFL_XXXXXX``,
        the address is:

        .. code-block::

            fcbgnasc.campusbiotech.ch/fcbgdata/0000_CBT_EPFL_XXXXXX

    .. tab-item:: EPFL

        If you are connected to the EPFL network, the domain is ``epfl.ch``. For
        example, for the share ``0000_CBT_EPFL_XXXXXX``, the address is:

        .. code-block::

            fcbgnasc.epfl.ch/fcbgdata/0000_CBT_EPFL_XXXXXX

    .. tab-item:: UniGE

        If you are connected to the UniGE network, the domain is ``unige.ch``. For
        example, for the share ``0000_CBT_EPFL_XXXXXX``, the address is:

        .. code-block::

            fcbgnasc.unige.ch/fcbgdata/0000_CBT_EPFL_XXXXXX

Once the address and credentials are known, mounting the network share differs depending
on the OS. On the ``meguser`` account of the
:ref:`stimulation PC <stim-pc:Stimulation PC>` and
:ref:`data analysis PC <data-analysis-pc:Data analysis PC (DANA)>`, you can find a PDF
describing the mounting procedure on the desktop.

.. tab-set::

    .. tab-item:: Windows

        On Windows, you can mount a network drive in the file explorer from ``This PC``.
        In the menu bar, select ``Computer`` and ``Map network drive``. Choose an
        available drive letter, set the field ``Folder`` to ``\\$(address)`` where
        ``$(address)`` is replaced with the network share address, and tick
        ``Connect using different credentials``.

        .. code-block::

            \\fcbgnasc.campusbiotech.ch\fcbgdata

        .. image:: ./_static/isilon/windows-address.png
            :align: center
            :width: 600

        .. important::

            On the :ref:`stimulation PC <stim-pc:Stimulation PC>` please deselect
            ``Reconnect at sign-in``.

        A pop-up will request your credentials. Enter your username and password.

        .. image:: ./_static/isilon/windows-credentials-dark.png
            :align: center
            :class: only-dark
            :width: 400

        .. image:: ./_static/isilon/windows-credentials-light.png
            :align: center
            :class: only-light
            :width: 400

        .. important::

            On the :ref:`stimulation PC <stim-pc:Stimulation PC>` do not save the
            password. Please deselect ``Remember my credentials``.

        The network share is now mounted and appears in the left pane as a network
        drive.

        .. image:: ./_static/isilon/windows-connected-dark.png
            :align: center
            :class: only-dark

        .. image:: ./_static/isilon/windows-connected-light.png
            :align: center
            :class: only-light

        .. important::

            On the :ref:`stimulation PC <stim-pc:Stimulation PC>` please disconnect the
            network drive when you are leaving.

    .. tab-item:: macOS

        On macOS, ``Finder`` can connect to network share. After opening it, hit
        ``Cmd + K``, or select ``Go`` and ``Connect to Server...`` to open the
        corresponding pop-up. In the address field, enter ``smb://$(address)`` where
        ``$(address)`` is replaced with the network share address. For instance:

        .. code-block::

            smb://fcbgnasc.epfl.ch/fcbgdata

        .. image:: ./_static/isilon/macos-address-dark.png
            :align: center
            :class: only-dark

        .. image:: ./_static/isilon/macos-address-light.png
            :align: center
            :class: only-light

        A pop-up will request your credentials. Select ``Registered User``, enter your
        username and password.

        .. image:: ./_static/isilon/macos-credentials-dark.png
            :align: center
            :class: only-dark

        .. image:: ./_static/isilon/macos-credentials-light.png
            :align: center
            :class: only-light

        The network share is now mounted and appears in the left pane as an external
        drive.

        .. image:: ./_static/isilon/macos-connected-dark.png
            :align: center
            :class: only-dark

        .. image:: ./_static/isilon/macos-connected-light.png
            :align: center
            :class: only-light

    .. tab-item:: Linux

        Mounting the network share might differ depending on your Linux distribution.
        For an Ubuntu-based distribution, the network share can be mounted from the
        ``nautilus`` file explorer. It requires ``smbclient`` to be installed.

        .. code-block:: bash

            $ sudo apt install smbclient

        In the left pane of the file explorer, select ``Other locations``. At the
        bottom, in the field ``Connect to Server``, enter ``smb://$(address)`` where
        ``$(address)`` is replaced with the network share address. For instance:

        .. code-block::

            smb://fcbgnasc.campusbiotech.ch/fcbgdata

        .. image:: ./_static/isilon/linux-address-dark.png
            :align: center
            :class: only-dark

        .. image:: ./_static/isilon/linux-address-light.png
            :align: center
            :class: only-light

        A pop-up will request your credentials. Select ``Registered User``, enter your
        username, domain (``campusbiotech.ch``, ``epfl.ch`` or ``unige.ch``) and
        password.

        .. image:: ./_static/isilon/linux-credentials-dark.png
            :align: center
            :class: only-dark

        .. image:: ./_static/isilon/linux-credentials-light.png
            :align: center
            :class: only-light

        .. important::

            On the :ref:`stimulation PC <stim-pc:Stimulation PC>` or the
            :ref:`data analysis PC <data-analysis-pc:Data analysis PC (DANA)>`, do not
            save the password. Please select ``Forget password immediately`` or
            ``Remember password until you logout``.

        The network share is now mounted and appears in the left pane as an external
        drive.

        .. image:: ./_static/isilon/linux-connected-dark.png
            :align: center
            :class: only-dark

        .. image:: ./_static/isilon/linux-connected-light.png
            :align: center
            :class: only-light

        .. important::

            On the :ref:`stimulation PC <stim-pc:Stimulation PC>` or the
            :ref:`data analysis PC <data-analysis-pc:Data analysis PC (DANA)>`, please
            eject (disconnect) the network share when you are leaving.

        .. tip::

            If you want to mount the network share automatically, e.g. on boot, you can
            edit ``/etc/fstab`` and use ``cifs``.

            .. code-block:: bash

                $ sudo apt install cifs-utils
                $ sudo mkdir /mnt/Isilon  # location in which the share is mounted
                $ sudo nano /etc/fstab

            In the ``fstab``, add a line:

            .. code-block::

                //fcbgnasc.$(network).ch/fcbgdata/$(share)  /mnt/Isilon  cifs  credentials=/root/.smbcredentials,uid=$(user),gid=$(user),file_mode=0770,dir_mode=0770  0  0

            Where ``$(network)`` is replaced by the network you are connected to,
            ``$(share)`` is replaced by the share name, ``$(user)`` is replaced by your
            username. The credentials have to be defined in ``/root/.smbcredentials``:

            .. code-block::

               username=...
               password=...
               domain=...  # campusbiotech.ch, epfl.ch or unige.ch

            If you are using ``systemd``, you can add the flags:

            - ``x-systemd.automount`` to automatically mount the share if it was not
              already available when you navigate to ``/mnt/Isilon``.
            - ``x-systemd.after=network-online.target`` to mount only after the target
              network is connected.
