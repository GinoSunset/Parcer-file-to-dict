from contextlib import contextmanager
from io import TextIOWrapper
from collections import defaultdict
import re

key_value_string_re = re.compile(r"^\S.+:.*")


@contextmanager
def open_parse_file(path: str) -> TextIOWrapper:
    try:
        file = open(path, "r")
        yield file
    finally:
        if file:
            file.close()


def parse_file(path):
    documents = []
    current_docs = {}
    key = ""
    with open_parse_file(path) as file:
        for line in file:
            if line.startswith("#"):
                continue
            if line == "\n" or line == "\r\n":
                if current_docs != {}:
                    documents.append(current_docs)
                    current_docs = {}
                continue
            if re.match(key_value_string_re, line):
                key, value = line.split(":", 1)
                value = value.lstrip().rstrip("\n")
                if key in current_docs:
                    current_docs[key] += "\n" + value
                    continue
                current_docs[key] = value
                continue
            current_docs[key] += "\n" + line.lstrip().rstrip("\n")
    return documents


def load_data(path):
    parsed_data = parse_file(path)

    for document in parsed_data:
        ...
        # load document to database (or do something else)
