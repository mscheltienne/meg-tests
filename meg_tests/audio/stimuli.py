from bsl.triggers import ParallelPortTrigger
from psychopy.clock import wait
from stimuli.audio import Tone


def run(address: str, frequency: float) -> None:
    """Run a loop of 100 pure tone auditory stimuli.

    Before each stimuli, a trigger is delviered on the first pin of the DB-25
    parallel port. The trigger is not compensated for the stimuli delay.
    `stimuli.Tone` is used to play the auditory stimuli using ``sounddevice``.

    Parameters
    ----------
    address : str
    frequency : float
        Frequency of the auditory stimuli. The frequency should be chosen based
        on the sampling rate selected on the DACQ.
    """
    trigger = ParallelPortTrigger(address)
    sound = Tone(volume=20, frequency=frequency)

    n = 1
    while n <= 100:
        trigger.signal(1)
        sound.play()
        wait(1, hogCPUperiod=0.2)

    del sound
    del trigger
