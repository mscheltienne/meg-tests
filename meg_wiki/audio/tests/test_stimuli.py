import time
from logging import INFO

from meg_wiki import logger, set_log_level
from meg_wiki.audio.stimuli import sounddevice_uncompensated

logger.propagate = True


def test_sounddevice_uncompensated(caplog):
    """Test execution of sounddevice_uncompensated."""
    set_log_level(INFO)
    caplog.set_level(INFO)
    caplog.clear()
    start = time.time()
    sounddevice_uncompensated("mock", 1000, volume=10, n_repetition=2)
    end = time.time()
    assert "Event 1 / 2" in caplog.text
    assert "Event 2 / 2" in caplog.text
    assert 2 <= (end - start)
