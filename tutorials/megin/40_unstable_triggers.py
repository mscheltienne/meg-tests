"""
.. _tut-unstable-triggers:

Unstable triggers
=================

Rarely, triggers delivered to the MEG system can be "unstable" and not form perfect
square pulses. This can be due to a variety of reasons, such as a bad connection between
the trigger I/O box and the MEG system.

Those instabilities can yield to missing triggers when automatically parsing the
``"stim"`` channels with default arguments. In this example, we will show case the
problem and how to parse those unstable triggers.
"""
