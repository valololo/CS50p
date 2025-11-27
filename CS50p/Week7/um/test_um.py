from um import count


def test_count_no_um():
    assert count("This is a test.") == 0
    assert count("Look at my new album.") == 0


def test_count_single_um():
    assert count("Um, this is a test.") == 1
    assert count("Um, look at my new album.") == 1


def test_count_multiple_um():
    assert count("Um, I think um we should um go.") == 3
    assert count("Um um um!") == 3
    assert count("This is um a test with um multiple albums.") == 2


def test_count_case_insensitivity():
    assert count("um, this is a test.") == 1
    assert count("UM, this is a test.") == 1
    assert count("Um, this is a test.") == 1
    assert count("uM, this is a test.") == 1
