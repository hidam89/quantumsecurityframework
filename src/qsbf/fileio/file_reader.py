"""
file_reader.py

Utility for reading files.
"""

from pathlib import Path


class FileReader:

    def read(self, file_path):

        path = Path(file_path)

        with open(path, "rb") as f:
            return f.read()
