from pathlib import Path as Path
from typing import Union

from .datasets import sample as sample

def load_mapping(fname: Union[str, Path]) -> dict[str, str]:
    """Load a mapping TXT file into an MNE-compatible dictionary.

    The loaded mapping can be used to rename the channels from a recording with
    ``inst.rename_channels(mapping)``.

    .. code-block:: python

        fname = "mapping.txt"
        mapping = load_mapping(fname)
        raw.rename_channels(mapping)

    Parameters
    ----------
    fname : str | Path
        Path to the TXT file containing the mapping to load. Each line yields
        one channels formatted as ``old: new``.

    Returns
    -------
    mapping : dict
        A dictionary mapping the old channel name to the new channel name.
    """

def load_mapping_32chs() -> dict[str, str]:
    """Load the mapping dictionary for the 32 chs cap.

    .. code-block:: python

        mapping = load_mapping_32chs()
        raw.rename_channels(mapping)

    Returns
    -------
    mapping : dict
        A dictionary mapping the old channel name to the new channel name.
    """

def load_mapping_64chs() -> dict[str, str]:
    """Load the mapping dictionary for the 64 chs cap.

    .. code-block:: python

        mapping = load_mapping_64chs()
        raw.rename_channels(mapping)

    Returns
    -------
    mapping : dict
        A dictionary mapping the old channel name to the new channel name.
    """

def load_mapping_128chs() -> dict[str, str]:
    """Load the mapping dictionary for the 128 chs cap.

    .. code-block:: python

        mapping = load_mapping_128chs()
        raw.rename_channels(mapping)

    Returns
    -------
    mapping : dict
        A dictionary mapping the old channel name to the new channel name.
    """