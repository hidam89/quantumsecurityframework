from src.qsbf.rsa.rsa_algorithm import RSAAlgorithm


def main():

    rsa = RSAAlgorithm(2048)

    rsa.initialize()

    plaintext = b"Quantum Safe Security Framework"

    ciphertext = rsa.encrypt(plaintext)

    recovered = rsa.decrypt(ciphertext)

    print("=" * 60)
    print("RSA ALGORITHM TEST")
    print("=" * 60)

    print()

    print("Original :", plaintext)

    print()

    print("Recovered:", recovered)

    print()

    print("Integrity:", plaintext == recovered)


if __name__ == "__main__":
    main()