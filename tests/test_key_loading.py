from src.qsbf.rsa.key_generator import RSAKeyGenerator
from src.qsbf.rsa.key_manager import RSAKeyManager


def main():

    generator = RSAKeyGenerator(2048)

    private_key, public_key = generator.generate()

    manager = RSAKeyManager()

    manager.save_keys(
        private_key,
        public_key,
        2048,
    )

    loaded_private = manager.load_private_key(2048)

    loaded_public = manager.load_public_key(2048)

    print("=" * 60)
    print("RSA KEY LOADING SUCCESSFUL")
    print("=" * 60)

    print(type(loaded_private))

    print(type(loaded_public))


if __name__ == "__main__":
    main()