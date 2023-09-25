from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Dict, Union


def load_mapping(fname: Union[str, Path]) -> Dict[str, str]:
    """Load a mapping TXT file into an MNE-compatible dictionary.

    The loaded mapping can be used to rename the channels from a recording with
    ``inst.rename_channels(mapping)``.

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
    with open(fname, "r") as file:
        lines = file.readlines()

    lines = [
        [elt.strip() for elt in line.split("\n")[0].split(":")]
        for line in lines
        if line.startswith("EEG")
    ]
    mapping = {elt[0]: elt[1] for elt in lines}
    return mapping
