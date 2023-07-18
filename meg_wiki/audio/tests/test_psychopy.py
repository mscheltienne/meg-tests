import time
from logging import INFO

from meg_wiki import logger, set_log_level
from meg_wiki.audio.psychopy import psychopy_compensated, psychopy_uncompensated

logger.propagate = True


def test_psychopy_uncompensated(caplog):
    """Test execution of psychopy_uncompensated."""
    set_log_level(INFO)
    caplog.set_level(INFO)
    caplog.clear()
    start = time.time()
    psychopy_uncompensated("mock", 1000, volume=0.1, n_repetition=2)
    end = time.time()
    assert "Event 1 / 2" in caplog.text
    assert "Event 2 / 2" in caplog.text
    assert 2 <= (end - start)


def test_psychopy_compensated(caplog):
    """Test execution of psychopy_compensated."""
    set_log_level(INFO)
    caplog.set_level(INFO)
    caplog.clear()
    start = time.time()
    psychopy_compensated("mock", 1000, volume=0.1, n_repetition=2)
    end = time.time()
    assert "Event 1 / 2" in caplog.text
    assert "Event 2 / 2" in caplog.text
    assert 2 <= (end - start)
