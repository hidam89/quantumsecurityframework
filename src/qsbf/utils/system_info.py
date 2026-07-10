import json
import platform
import sys
from datetime import datetime
from pathlib import Path

import psutil


class SystemInfo:

    def collect(self):

        info = {

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "operating_system": platform.system(),

            "os_version": platform.version(),

            "architecture": platform.machine(),

            "processor": platform.processor(),

            "python_version": sys.version,

            "physical_cores": psutil.cpu_count(logical=False),

            "logical_cores": psutil.cpu_count(logical=True),

            "cpu_frequency_mhz": psutil.cpu_freq().max,

            "total_ram_gb": round(
                psutil.virtual_memory().total / (1024 ** 3),
                2,
            ),
        }

        return info

    def save(self):

        info = self.collect()

        Path("results").mkdir(exist_ok=True)

        output = Path("results/system_information.json")

        with open(output, "w") as file:

            json.dump(info, file, indent=4)

        return info