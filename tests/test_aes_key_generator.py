from src.qsbf.aes.key_generator import AESKeyGenerator


def main():

    generator = AESKeyGenerator(32)

    key = generator.generate()

    print("=" * 60)
    print("AES KEY GENERATION")
    print("=" * 60)

    print("Key Length:", len(key), "bytes")
    print("Key:", key.hex())


if __name__ == "__main__":
    main()