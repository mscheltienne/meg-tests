from ..utils._checks import ensure_int as ensure_int
from ..utils._docs import fill_doc as fill_doc
from ..utils._imports import import_optional_dependency as import_optional_dependency
from ..utils.logs import logger as logger

def sounddevice_uncompensated(address: str, frequency: float, volume: float=20, n_repetition: int=100) -> None:
    """Run a loop of pure tone auditory stimuli using sounddevice through stimuli.

    Before each stimuli, a trigger is delivered on the first pin of the DB-25
    parallel port. The trigger is not compensated for the stimuli delay.
    `stimuli.Tone` is used to play the auditory stimuli using ``sounddevice``.

    Parameters
    ----------
    address : str | ``'mock'``
        Address of the computer parallel port.
    frequency : float
        Frequency of the auditory stimuli. The frequency should be chosen based
        on the sampling rate selected on the DACQ.
    volume : float
        Volume at which the sound is played, between 0 and 100.
    n_repetitionn : int
        Number of sound repetition.

    Notes
    -----
    The sound duration is set to 200 ms.
    """