"""
file_writer.py

Utility for writing files.
"""

from pathlib import Path


class FileWriter:

    def write(self, file_path, data):

        path = Path(file_path)

        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "wb") as f:
            f.write(data)
