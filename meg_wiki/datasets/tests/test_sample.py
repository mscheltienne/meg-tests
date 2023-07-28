from importlib.resources import files

import pooch

from meg_wiki.datasets import sample


def test_sample(tmp_path):
    """Test download of the sample dataset."""
    path = sample.data_path()  # retrieve dataset

    # compare with the registry
    registry = files("meg_wiki.datasets") / "sample-registry.txt"
    fetcher = pooch.create(path=None, base_url="")
    fetcher.load_registry(registry)
    for file, hash_ in fetcher.registry.items():
        assert (path / file).exists()
        assert pooch.file_hash(path / file) == hash_
    del fetcher

    # create a new registry
    output = tmp_path / "registry-1.txt"
    pooch.make_registry(path, output=output, recursive=True)
    assert pooch.file_hash(output) == pooch.file_hash(registry)
    output = tmp_path / "registry-2.txt"
    sample._make_registry(output)
    assert pooch.file_hash(output) == pooch.file_hash(registry)
