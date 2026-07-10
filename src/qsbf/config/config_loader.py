import json
from pathlib import Path


class ConfigLoader:

    def __init__(self, config_path="configs/config.json"):
        self.config_path = Path(config_path)

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with open(self.config_path, "r") as file:
            self.config = json.load(file)

    def get(self, key):

        return self.config.get(key)

    def show(self):

        for key, value in self.config.items():
            print(f"{key:25} : {value}")