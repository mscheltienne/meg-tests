from bsl.triggers import ParallelPortTrigger
from psychopy.clock import wait
from stimuli.audio import Tone

from ..utils._checks import ensure_int
from ..utils.logs import logger


def run(address: str, frequency: float, volume: float = 20, n: int = 100) -> None:
    """Run a loop of pure tone auditory stimuli using sounddevice through stimuli.

    Before each stimuli, a trigger is delivered on the first pin of the DB-25
    parallel port. The trigger is not compensated for the stimuli delay.
    `stimuli.Tone` is used to play the auditory stimuli using ``sounddevice``.

    Parameters
    ----------
    address : str
        Address of the computer parallel port.
    frequency : float
        Frequency of the auditory stimuli. The frequency should be chosen based
        on the sampling rate selected on the DACQ.
    volume : float
        Volume at which the sound is played, between 0 and 100.
    n : int
        Number of sound repetition.

    Notes
    -----
    The sound duration is set to 200 ms.
    """
    n = ensure_int(n, "n")
    # error checking on the arguments is handled by BSL and stimuli directly
    trigger = ParallelPortTrigger(address)
    sound = Tone(volume=volume, frequency=frequency, duration=0.2)

    for k in range(1, n + 1, 1):
        logger.info("Event %i / %i", k, n)
        trigger.signal(1)
        sound.play()
        wait(0.5, hogCPUperiod=0.2)

    del sound
    del trigger
