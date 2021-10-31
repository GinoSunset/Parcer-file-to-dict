from contextlib import contextmanager
import gzip
from io import TextIOWrapper
import re

key_value_string_re = re.compile(
    r"^\S.+:.*"
)  # does not start with a space character any characters separated by the ":" character


@contextmanager
def open_parse_file(path: str) -> TextIOWrapper:
    file = None
    xopen = gzip.open if path.endswith(".gz") else open
    try:
        file = xopen(path, "rt")
        yield file
    finally:
        if file:
            file.close()


def parse_file(path):
    documents = []
    current_docs = {}
    current_key = ""
    with open_parse_file(path) as file:
        for line in file:
            if is_comment_line(line):
                continue
            if is_separating_line(line):
                if current_docs != {}:
                    documents.append(current_docs)
                    current_docs = {}
                continue
            if is_line_with_key_value(line):
                current_key, line = line.split(":", 1)
            value = cleaned_value(line)
            update_current_docs(current_docs, current_key, value)
    return documents


def update_current_docs(current_docs: dict, key: str, value: str):
    if key in current_docs:
        current_docs[key] += "\n" + value
        return
    current_docs[key] = value


def cleaned_value(value: str):
    return value.lstrip().rstrip("\n")


def is_line_with_key_value(line: str):
    return re.match(key_value_string_re, line)


def is_separating_line(line: str):
    return line == "\n" or line == "\r\n"


def is_comment_line(line: str):
    return line.startswith("#")


def load_data(path):
    parsed_data = parse_file(path)

    for document in parsed_data:
        ...
        # load document to database (or do something else)
