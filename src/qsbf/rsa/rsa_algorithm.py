from src.qsbf.core.algorithm import Algorithm


class RSAAlgorithm(Algorithm):

    @property
    def name(self):
        return "RSA"

    def initialize(self):
        print("Initializing RSA")

    def generate_keys(self):
        return None

    def encrypt(self, plaintext: bytes):
        return plaintext

    def decrypt(self, ciphertext: bytes):
        return ciphertext

    def benchmark(self):
        return {}