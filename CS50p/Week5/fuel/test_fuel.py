from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50.0
    assert convert("3/4") == 75.0
    assert convert("2/5") == 40.0
    assert convert("0/1") == 0.0
    assert convert("1/1") == 100.0

def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_invalid_inputs():

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("3/2")

    with pytest.raises(ValueError):
        convert("a/b")

    with pytest.raises(ValueError):
        convert("-1/4")
