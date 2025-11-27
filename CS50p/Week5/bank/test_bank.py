from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("oy") == 100

def test_value_whitespace_case():
    assert value(" Hello") == 0
    assert value("HEY") == 20
    assert value("  oy  ") == 100

def test_value_punctiuation():
    assert value("hello!") == 0
    assert value("hmmm...") == 20
    assert value("oy123") == 100
