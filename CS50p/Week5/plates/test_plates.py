from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("AB123") == True
    assert is_valid("A1234") == False
    assert is_valid("1AB23") == False

def test_length_between_2_and_6():
    assert is_valid("AB") == True
    assert is_valid("ABCDE") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_only_letters_and_numbers():
    assert is_valid("AB123") == True
    assert is_valid("AB@123") == False
    assert is_valid("AB 123") == False
    assert is_valid("AB-123") == False

def test_no_letters_after_number():
    assert is_valid("AB123") == True
    assert is_valid("AB12C3") == False
    assert is_valid("AB1C23") == False
    assert is_valid("AB123C") == False

def test_no_leading_zeros_in_numbers():
    assert is_valid("AB123") == True
    assert is_valid("AB012") == False
    assert is_valid("AB001") == False
    assert is_valid("AB0") == False
