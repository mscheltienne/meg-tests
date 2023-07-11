from bsl.triggers import ParallelPortTrigger
from psychopy.clock import wait
from psychopy.sound import Sound

from ..utils._checks import check_type, ensure_int
from ..utils.logs import logger


def run(address: str, frequency: float, volume: float = 0.2, n: int = 100) -> None:
    """Run a loop of pure tone auditory stimuli using PsychoPy.

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
        Volume at which the sound is played, between 0 and 1.
    n : int
        Number of sound repetition.

    Notes
    -----
    The sound duration is set to 200 ms. The hanning window to smooth the onset and
    offset is disabled.
    """
    check_type(frequency, ("numeric",), "frequency")
    if frequency <= 0:
        raise ValueError("The sound frequency (Hz) must be a strictly positive number.")
    check_type(volume, ("numeric",), "volume")
    if volume < 0 or 1 < volume:
        raise ValueError("The volume must be defined between 0 and 1.")
    n = ensure_int(n, "n")
    # error checking on the parallel-port argument is handled by BSL directly
    trigger = ParallelPortTrigger(address)
    sound = Sound(value=frequency, volume=volume, secs=0.2, hamming=False)

    for k in range(1, n + 1, 1):
        logger.info("Event %i / %i", k, n)
        trigger.signal(1)
        sound.play()
        wait(0.5, hogCPUperiod=0.3)

    del sound
    del trigger
