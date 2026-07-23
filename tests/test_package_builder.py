from src.qsbf.hybrid.metadata import HybridMetadata
from src.qsbf.hybrid.package_builder import HybridPackageBuilder
from src.qsbf.hybrid.package_parser import HybridPackageParser


def main():

    metadata = HybridMetadata(
        version="1.0",
        algorithm="Hybrid RSA-AES",
        rsa_key_size=2048,
        aes_key_size=256,
        nonce_length=12,
        encrypted_key_length=256,
        ciphertext_length=1024,
    )

    builder = HybridPackageBuilder()

    package = builder.build(
        metadata=metadata,
        nonce=b"123456789012",
        encrypted_key=b"encrypted_key",
        ciphertext=b"ciphertext",
    )

    parser = HybridPackageParser()

    (
        parsed_metadata,
        nonce,
        encrypted_key,
        ciphertext,
    ) = parser.parse(package)

    print("=" * 60)
    print("PACKAGE TEST")
    print("=" * 60)

    print(parsed_metadata)
    print(nonce)
    print(encrypted_key)
    print(ciphertext)


if __name__ == "__main__":
    main()