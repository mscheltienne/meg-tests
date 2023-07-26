MEG settings
============

Sampling rate
-------------

The MEG default sampling rate is 1 kHz, but it can be changed to [...].

Channel selection
-----------------

Internal Active Shielding (IAS)
-------------------------------

Internal active shielding is used to compensante environmental noise through magnetic
fields induced in 6 coils in the walls, floor and ceiling of the magnetically shielded
room (MSR). On our site, the environmental noise is very low. Thus it is recommended to
keep the internal active shielding disabled.

The 6 coils can compensante the homogeneous fields :math:`B_x`, :math:`B_y`,
:math:`B_z` and the diagonal uniform gradients
:math:`\frac{\partial{B_x}}{\partial{x}}`, :math:`\frac{\partial{B_y}}{\partial{y}}`,
:math:`\frac{\partial{B_z}}{\partial{z}}`. The coils emit a magnetic fields which drives
18 magnetometers to 0:

- In the ``x+`` direction (right of the helmet): 1311, 1321, 1331, 1341
- In the ``x-`` direction (left of the helmet): 0211, 0221, 0231, 0241
- In the ``y+`` direction (front of the helmet): 0811, 0812
- In the ``y-`` direction (rear of the helmet): 2111, 2121, 2131, 2141
- In the ``z`` direction (top of the helmet): 0711, 0721, 0731, 0741

.. note::

    Note that those 6 coils are *inside* the MSR and thus add an interference
    source inside the MSR. Recordings using internal active shielding must use
    :ref:`data-analysis-pc:MaxWell filter` to restore the original field pattern.

The IAS compensation channels can be recorded and include:

- The current through the individual coils, in room coordinate: ``IASX-``, ``IASX+``,
  ``IASY-``, ``IASY+``, ``IASZ-``, ``IASZ+``.
- The virtual compensation channel which represents the feedback required to cancel the
  uniform field and the diagonal gradient components, in head coordinate: ``IAS_X``
  (:math:`B_x`), ``IAS_Y`` (:math:`B_y`), ``IAS_Z`` (:math:`B_z`), ``IAS_DX``
  (:math:`\frac{\partial{B_x}}{\partial{x}}`), ``IAS_DY``
  (:math:`\frac{\partial{B_y}}{\partial{y}}`).

.. note::

    ``IAS_DZ`` is missing because according to Maxwell's equation there are only 2
    independent diagonal uniform gradient components since the sum of the diagonal
    gradients is equal to 0:
    :math:`\frac{\partial{B_x}}{\partial{x}} + \frac{\partial{B_y}}{\partial{y}} +
    \frac{\partial{B_z}}{\partial{z}} = 0`
