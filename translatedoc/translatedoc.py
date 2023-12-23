#!/usr/bin/env python3
"""translatedoc - ドキュメントを翻訳するツール。"""
import argparse
import os
import pathlib
import sys
import typing

import openai
import tqdm

if typing.TYPE_CHECKING:
    from unstructured.documents.elements import Element


def main():
    """メイン関数。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_files", nargs="+", help="input files")
    parser.add_argument("--output", "-o", required=True, help="output file")
    parser.add_argument(
        "--language", "-l", default="Japanese", help="language (default: Japanese)"
    )
    parser.add_argument(
        "--model",
        "-m",
        default="gpt-3.5-turbo-1106",
        help="model (default: gpt-3.5-turbo-1106)",
    )
    args = parser.parse_args()

    if args.output == "-":
        exit_code = _translatedoc(sys.stdout, args)
    else:
        output_file = pathlib.Path(args.output).absolute()
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open("w", encoding="utf-8") as file:
            exit_code = _translatedoc(file, args)

    sys.exit(exit_code)


def _translatedoc(file: typing.TextIO, args: argparse.Namespace) -> int:
    """処理。"""
    openai_client = openai.OpenAI(base_url=os.environ.get("OPENAI_API_URL"))

    for input_file in tqdm.tqdm(args.input_files, desc="Input files"):
        if len(args.input_files) > 1:
            file.write(f"{'#' * 32} {input_file} {'#' * 32}\n")

        try:
            chunks = _load_document(input_file)
            for chunk in tqdm.tqdm(chunks, desc="Chunks"):
                output_chunk = _translate(str(chunk), args, openai_client)
                file.write(output_chunk.strip() + "\n\n")
                file.flush()
        except Exception as e:
            print(f"Error: {e} ({input_file})", file=sys.stderr)
            return 1

        file.write("\n")
    return 0


def _load_document(input_file: str) -> "list[Element]":
    """ドキュメントの読み込み・パース。"""
    from unstructured.chunking.title import chunk_by_title
    from unstructured.partition.auto import partition

    if input_file.startswith("http://") or input_file.startswith("https://"):
        elements = partition(url=input_file)
    else:
        elements = partition(filename=input_file)
    chunks = chunk_by_title(elements, max_characters=4096)
    return chunks


def _translate(
    chunk: str, args: argparse.Namespace, openai_client: openai.OpenAI
) -> str:
    """翻訳。"""
    response = openai_client.chat.completions.create(
        model=args.model,
        messages=[
            {
                "role": "system",
                "content": f"Translate the input into {args.language}."
                " Do not output anything other than the translation result.",
            },
            {"role": "user", "content": chunk},
        ],
        temperature=0.0,
    )
    assert response.choices[0].message.content is not None
    return response.choices[0].message.content


if __name__ == "__main__":
    main()
