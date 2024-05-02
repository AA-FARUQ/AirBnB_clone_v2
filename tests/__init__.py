#!/usr/bin/python3
"""Unit tests for the AirBnb clone modules."""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_text_stream(text_stream: TextIO):
    """Clears the contents of a given text stream.
    Args:
        text_stream (TextIO): The text stream to clear.
    """
    if text_stream.seekable():
        text_stream.seek(0)
        text_stream.truncate(0)


def delete_exiting_file(file_path: str):
    """Removes a file if it exists.
    Args:
        file_path (str): The path to the file to remove.
    """
    if os.path.isfile(file_path):
        os.unlink(file_path)


def reset_storage(store: FileStorage, storage_file='file.json'):
    """Resets the items in the given storage.
    Args:
        store (FileStorage): The FileStorage to reset.
        storage_file (str): The path to the storage file.
    """
    with open(storage_file, mode='w') as file:
        file.write('{}')
    if store is not None:
        store.reload()


def read_file_contents(file_name):
    """Reads the contents of a given file.
    Args:
        file_name (str): The name of the file to read.
    Returns:
        str: The contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


def write_to_file(file_name, text):
    """Writes a text to a given file.
    Args:
        file_name (str): The name of the file to write to.
        text (str): The content to write to the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)
