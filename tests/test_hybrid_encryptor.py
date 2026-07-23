from src.qsbf.rsa.rsa_algorithm import RSAAlgorithm
from src.qsbf.hybrid.hybrid_encryptor import HybridEncryptor


def main():

    rsa = RSAAlgorithm(2048)

    rsa.initialize()

    hybrid = HybridEncryptor(rsa)

    plaintext = b"This is my first Hybrid Encryption."

    package = hybrid.encrypt(plaintext)

    print("=" * 60)
    print("HYBRID ENCRYPTION")
    print("=" * 60)

    print()

    print(package["metadata"])

    print()

    print("Nonce Length :", len(package["nonce"]))

    print("Encrypted AES Key :", len(package["encrypted_key"]))

    print("Ciphertext Length :", len(package["ciphertext"]))


if __name__ == "__main__":
    main()