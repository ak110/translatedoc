"""テストコード。"""

import translatedoc


def test_partition1():
    """分割テストその1。"""
    text = """
a a a

a a a

a

a
"""
    chunks = translatedoc.partition(text.strip(), "gpt-3.5-turbo", max_chunk_size=5)
    assert chunks == ["a a a", "a a a\n\na", "a"], repr(chunks)


def test_partition():
    """分割テストその2。"""
    text = """
a a a

b b b b b b

とてもとても長いテキスト
"""
    chunks = translatedoc.partition(text.strip(), "gpt-3.5-turbo", max_chunk_size=5)
    assert chunks == [
        "a a a",
        "b b ",
        "b b ",
        "b b",
        "とてもとて",
        "も長いテ",
        "キスト",
    ], repr(chunks)
