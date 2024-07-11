from feul import convert,gauge
import pytest
def test_convert():
    assert convert("1/2")==50
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError): 
        convert("1/0")

def test_gauge():
    assert gauge(50)=="50%"
    assert gauge(100)=="F"
    assert gauge(0)=="E"
    assert gauge(1)=="E"
    assert gauge(99)=="F"