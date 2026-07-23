from src.qsbf.aes.key_generator import AESKeyGenerator
from src.qsbf.aes.encryptor import AESEncryptor
from src.qsbf.aes.decryptor import AESDecryptor


def main():

    generator = AESKeyGenerator(32)

    key = generator.generate()

    encryptor = AESEncryptor()

    decryptor = AESDecryptor()

    plaintext = b"Quantum Security Benchmark Framework"

    nonce, ciphertext = encryptor.encrypt(
        key,
        plaintext,
    )

    recovered = decryptor.decrypt(
        key,
        nonce,
        ciphertext,
    )

    print("=" * 60)
    print("AES ENCRYPTION / DECRYPTION")
    print("=" * 60)

    print()

    print("Original :", plaintext)

    print()

    print("Recovered:", recovered)

    print()

    print("Integrity:", plaintext == recovered)

    print()

    print("Plaintext Size :", len(plaintext))

    print("Ciphertext Size:", len(ciphertext))

    print("Nonce Size     :", len(nonce))

    print("AES Key Size   :", len(key) * 8, "bits")


if __name__ == "__main__":
    main()