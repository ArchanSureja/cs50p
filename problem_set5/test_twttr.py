from twttr import shorten 

def test_shorten():
    assert shorten("twitter")=="twttr"
    assert shorten("hello")=="hll"
    assert shorten("GOOD MORNING")=="GD MRNNG"