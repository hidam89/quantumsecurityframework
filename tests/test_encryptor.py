from src.qsbf.rsa.key_generator import RSAKeyGenerator
from src.qsbf.rsa.encryptor import RSAEncryptor


def main():

    generator = RSAKeyGenerator(2048)

    private_key, public_key = generator.generate()

    encryptor = RSAEncryptor()

    plaintext = b"Hello Quantum Security Framework"

    ciphertext = encryptor.encrypt(
        public_key,
        plaintext,
    )

    print("=" * 60)
    print("RSA ENCRYPTION SUCCESSFUL")
    print("=" * 60)

    print("Plaintext Length :", len(plaintext))

    print("Ciphertext Length:", len(ciphertext))


if __name__ == "__main__":
    main()