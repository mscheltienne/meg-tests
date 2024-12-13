Manual sensor tuning
====================

In manual tuning, the channel response curve should be:

- (1) a sinusoids
- (2) as large PTP amplitude as possible
- (3) with the 0 from the Y-axis crossing at 1/3 from the bottom

The BIAS controls the amplitude and the shape to some degree, the OFFSET the Y-axis
crossing and the GATE controls the shape to some degree. The GATE should rarely be
modified.

.. tab-set::

    .. tab-item:: Good tuning

        .. image:: ../_static/tuning/good.png
            :align: right
            :class: img-with-border
            :width: 100%

    .. tab-item:: Bad BIAS

        .. image:: ../_static/tuning/bad_bias.png
            :align: right
            :class: img-with-border
            :width: 100%

    .. tab-item:: Bad OFFSET

        .. image:: ../_static/tuning/bad_offset.png
            :align: right
            :class: img-with-border
            :width: 100%

    .. tab-item:: Bad GATE

        .. image:: ../_static/tuning/bad_gate.png
            :align: right
            :class: img-with-border
            :width: 100%
