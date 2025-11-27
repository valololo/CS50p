from twttr import shorten

def test_shorten():
    tests = {"twitter": "twttr", "youtube": "ytb", "instagram": "nstgrm"}

    for key, expected in tests.items():
        assert shorten(key) == expected

    edges = {"TWITTER": "TWTTR", "youtube.": "ytb.", "instagram10": "nstgrm10"}

    for key, expected in edges.items():
        assert shorten(key) == expected
