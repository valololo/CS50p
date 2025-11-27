from working import convert
import pytest


def test_convert_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 5 PM") == "00:00 to 17:00"
    assert convert("12:00 PM to 1:00 AM") == "12:00 to 01:00"
    assert convert("11 AM to 12 PM") == "11:00 to 12:00"


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("09 AM to 5:001 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 5")
