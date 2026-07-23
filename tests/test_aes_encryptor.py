from src.qsbf.aes.key_generator import AESKeyGenerator
from src.qsbf.aes.encryptor import AESEncryptor


def main():

    generator = AESKeyGenerator(32)

    key = generator.generate()

    encryptor = AESEncryptor()

    plaintext = b"Quantum Safe Security Framework"

    nonce, ciphertext = encryptor.encrypt(
        key,
        plaintext,
    )

    print("=" * 60)
    print("AES ENCRYPTION")
    print("=" * 60)

    print("Plaintext Length :", len(plaintext))

    print("Ciphertext Length:", len(ciphertext))

    print("Nonce Length     :", len(nonce))


if __name__ == "__main__":
    main()