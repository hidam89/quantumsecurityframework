from src.qsbf.rsa.key_generator import RSAKeyGenerator
from src.qsbf.rsa.key_manager import RSAKeyManager


def main():

    generator = RSAKeyGenerator(2048)

    private_key, public_key = generator.generate()

    manager = RSAKeyManager()

    private_path, public_path = manager.save_keys(
        private_key,
        public_key,
        2048
    )

    print("=" * 50)
    print("RSA KEYS SAVED SUCCESSFULLY")
    print("=" * 50)

    print("Private Key:", private_path)

    print("Public Key :", public_path)


if __name__ == "__main__":
    main()