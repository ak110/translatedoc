# translatedoc

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Lint&Test](https://github.com/ak110/translatedoc/actions/workflows/python-app.yml/badge.svg)](https://github.com/ak110/translatedoc/actions/workflows/python-app.yml)
[![PyPI version](https://badge.fury.io/py/translatedoc.svg)](https://badge.fury.io/py/translatedoc)

PDFなどのドキュメントを翻訳するツール。

[Unstructured](https://unstructured.io/)で読み込み、OpenAI APIに渡しているだけ。

## インストール

### 1. Unstructured

インストール例:

```bash
sudo apt install poppler-utils poppler-data tesseract-ocr tesseract-ocr-jpn
pip install unstructured[all-docs] --extra-index-url https://download.pytorch.org/whl/cu118
```

`cu118`のところは環境に合わせて変更する。

詳細は[Unstructuredのドキュメント](https://unstructured-io.github.io/unstructured/installing.html)を参照。

### 2. translatedoc

```bash
pip install translatedoc
```

## 使い方

```bash
# export OPENAI_API_BASE=<your_api_base>  # default: https://api.openai.com/v1
export OPENAI_API_KEY=<your_api_key>
translatedoc --language=Japanese <input_files_and_or_urls>
```

カレントディレクトリに`ファイル名.Source.txt`と`ファイル名.Japanese.txt`が生成される。

詳細は `translatedoc --help` を参照。
