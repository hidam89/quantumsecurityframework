from src.qsbf.core.algorithm import Algorithm


class DummyAlgorithm(Algorithm):

    @property
    def name(self):
        return "Dummy"

    def initialize(self):
        print("Initialize")

    def generate_keys(self):
        print("Generate Keys")

    def encrypt(self, plaintext: bytes):
        return plaintext

    def decrypt(self, ciphertext: bytes):
        return ciphertext

    def benchmark(self):
        return {}


def main():

    algorithm = DummyAlgorithm()

    print(algorithm.name)

    algorithm.initialize()


if __name__ == "__main__":

    main()