from src.qsbf.aes.aes_algorithm import AESAlgorithm


def main():

    aes = AESAlgorithm()

    aes.initialize()

    plaintext = b"Quantum Security Benchmark Framework"

    encrypted = aes.encrypt(plaintext)

    recovered = aes.decrypt(encrypted)

    print("=" * 60)
    print("AES ALGORITHM TEST")
    print("=" * 60)

    print()

    print("Original :")

    print(plaintext)

    print()

    print("Recovered:")

    print(recovered)

    print()

    print("Integrity:", plaintext == recovered)


if __name__ == "__main__":

    main()