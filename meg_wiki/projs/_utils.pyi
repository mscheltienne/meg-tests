from mne import Projection as Projection

def orthonormalize_proj(projs: list[Projection]) -> list[Projection]:
    """Transform the set of projector vectors into an orthonormal basis using SVD.

    Parameters
    ----------
    projs : list of Projection
        The projection operators.

    Returns
    -------
    projs : list of Projection
        The orthogonalized projection operators.
    """

def rename_proj(
    projs: list[Projection], position: int, combined: bool
) -> list[Projection]:
    """Rename the projection operators.

    Parameters
    ----------
    projs : list of Projection
        The projection operators.
    position : int
        The gantry position.
    combined : bool
        Whether the projection operators are combined through an orthonormalization.
    """
