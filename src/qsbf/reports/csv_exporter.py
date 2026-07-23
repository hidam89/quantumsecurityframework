"""
csv_exporter.py

Export benchmark results to CSV.
"""

import csv
from pathlib import Path


class CSVExporter:

    def export(self, filename: str, result):

        path = Path("results/csv") / filename

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        write_header = not path.exists()

        with open(
            path,
            "a",
            newline="",
            encoding="utf-8",
        ) as csvfile:

            writer = csv.DictWriter(
                csvfile,
                fieldnames=result.to_dict().keys()
            )

            if write_header:

                writer.writeheader()

            writer.writerow(
                result.to_dict()
            )