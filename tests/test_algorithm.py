import sys
from pathlib import Path

# Add the project root to the Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.qsbf.core.algorithm import Algorithm
from src.qsbf.core.algorithm import Algorithm


class DummyAlgorithm(Algorithm):

    @property
    def name(self):
        return "Dummy"

    def initialize(self):
        print("Initialize")

    def generate_keys(self):
        return None

    def encrypt(self, plaintext: bytes):
        return plaintext

    def decrypt(self, ciphertext: bytes):
        return ciphertext

    def benchmark(self):
        return {}


if __name__ == "__main__":
    algorithm = DummyAlgorithm()
    print(algorithm.name)
    algorithm.initialize()