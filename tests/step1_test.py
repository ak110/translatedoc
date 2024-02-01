"""テストコード。"""

import pathlib

import translatedoc

TEST_DATA_DIR = pathlib.Path(__file__).parent / "data"


def test_extract_text_markdown():
    """テキスト抽出テストその1。"""
    text = translatedoc.extract_text(TEST_DATA_DIR / "markdown.md")
    assert text == (TEST_DATA_DIR / "markdown.Source.txt").read_text()
