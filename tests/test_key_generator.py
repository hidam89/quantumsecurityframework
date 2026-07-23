from src.qsbf.rsa.key_generator import RSAKeyGenerator


def main():

    generator = RSAKeyGenerator(2048)

    private_key, public_key = generator.generate()

    print("=" * 50)
    print("RSA KEY GENERATION SUCCESSFUL")
    print("=" * 50)

    print("\nPrivate Key Type:")
    print(type(private_key))

    print("\nPublic Key Type:")
    print(type(public_key))


if __name__ == "__main__":
    main()