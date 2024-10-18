import pytest

from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("domain") == "dmn"
    assert shorten("h1ll0 w0rld") == "h1ll0 w0rld"
    assert shorten("h#llo w*rld!!!") == "h#ll w*rld!!!"
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_error():
    with pytest.raises(TypeError):
        shorten(1)
        shorten("@")
