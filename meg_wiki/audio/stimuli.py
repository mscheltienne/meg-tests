from ..utils._checks import ensure_int
from ..utils._docs import fill_doc
from ..utils._imports import import_optional_dependency
from ..utils.logs import logger


@fill_doc
def sounddevice_uncompensated(
    address: str, frequency: float, volume: float = 20, n_repetition: int = 100
) -> None:
    """Run a loop of pure tone auditory stimuli using sounddevice through stimuli.

    Before each stimuli, a trigger is delivered on the first pin of the DB-25
    parallel port. The trigger is not compensated for the stimuli delay.
    `stimuli.Tone` is used to play the auditory stimuli using ``sounddevice``.

    Parameters
    ----------
    %(address)s
    %(frequency)s
    volume : float
        Volume at which the sound is played, between 0 and 100.
    %(n_repetition)s

    Notes
    -----
    The sound duration is set to 200 ms.
    """
    import_optional_dependency("byte_triggers")
    import_optional_dependency("psychopy")
    import_optional_dependency("stimuli")

    from byte_triggers import MockTrigger, ParallelPortTrigger
    from psychopy.clock import wait
    from stimuli.audio import Tone

    n = ensure_int(n_repetition, "n_repetition")
    # error checking on the arguments is handled by BSL and stimuli directly
    trigger = MockTrigger() if address == "mock" else ParallelPortTrigger(address)
    sound = Tone(volume=volume, frequency=frequency, duration=0.2)

    for k in range(1, n_repetition + 1, 1):
        logger.info("Event %i / %i", k, n)
        trigger.signal(1)
        sound.play()
        wait(1, hogCPUperiod=0.2)

    del sound
    del trigger
