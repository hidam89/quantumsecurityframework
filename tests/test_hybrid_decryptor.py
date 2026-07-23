print("Starting test_hybrid_decryptor...")
from src.qsbf.rsa.rsa_algorithm import RSAAlgorithm

from src.qsbf.hybrid.hybrid_encryptor import HybridEncryptor
from src.qsbf.hybrid.hybrid_decryptor import HybridDecryptor


def main():

    rsa = RSAAlgorithm(2048)

    rsa.initialize()

    encryptor = HybridEncryptor(rsa)

    decryptor = HybridDecryptor(rsa)

    plaintext = b"Layered Quantum Safe Security Framework"

    package = encryptor.encrypt(plaintext)

    recovered = decryptor.decrypt(package)

    print("=" * 60)
    print("HYBRID RSA-AES TEST")
    print("=" * 60)

    print()

    print("Original :")

    print(plaintext)

    print()

    print("Recovered:")

    print(recovered)

    print()

    print("Integrity :", plaintext == recovered)

    print()

    print(package["metadata"])
if __name__ == "__main__":
    main()