from src.qsbf.rsa.key_generator import RSAKeyGenerator
from src.qsbf.rsa.encryptor import RSAEncryptor
from src.qsbf.rsa.decryptor import RSADecryptor


def main():

    generator = RSAKeyGenerator(2048)

    private_key, public_key = generator.generate()

    encryptor = RSAEncryptor()

    decryptor = RSADecryptor()

    plaintext = b"Hello Quantum Security Framework"

    ciphertext = encryptor.encrypt(
        public_key,
        plaintext,
    )

    recovered = decryptor.decrypt(
        private_key,
        ciphertext,
    )

    print("=" * 60)
    print("RSA ENCRYPTION / DECRYPTION SUCCESSFUL")
    print("=" * 60)

    print()

    print("Original Plaintext:")
    print(plaintext)

    print()

    print("Recovered Plaintext:")
    print(recovered)

    print()

    print("Match:", plaintext == recovered)



    print()
    print("Plaintext Size :", len(plaintext), "bytes")
    print("Ciphertext Size:", len(ciphertext), "bytes")
    print("RSA Key Size   :", private_key.key_size, "bits")


if __name__ == "__main__":
    main()