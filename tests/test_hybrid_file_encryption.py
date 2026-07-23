from pathlib import Path

from src.qsbf.rsa.rsa_algorithm import RSAAlgorithm
from src.qsbf.hybrid.file_encryptor import HybridFileEncryptor
from src.qsbf.hybrid.file_decryptor import HybridFileDecryptor


def main():

    rsa = RSAAlgorithm(2048)
    rsa.initialize()

    encryptor = HybridFileEncryptor(rsa)
    decryptor = HybridFileDecryptor(rsa)

    input_file = "data/plaintext/sample.txt"
    encrypted_file = "data/encrypted/sample.qsbf"
    decrypted_file = "data/decrypted/sample_decrypted.txt"

    encryptor.encrypt_file(
        input_file,
        encrypted_file,
    )

    decryptor.decrypt_file(
        encrypted_file,
        decrypted_file,
    )

    original = Path(input_file).read_bytes()
    recovered = Path(decrypted_file).read_bytes()

    print("=" * 60)
    print("HYBRID FILE ENCRYPTION TEST")
    print("=" * 60)

    print("Input File      :", input_file)
    print("Encrypted File  :", encrypted_file)
    print("Decrypted File  :", decrypted_file)

    print()

    print("Original Size   :", len(original), "bytes")
    print("Recovered Size  :", len(recovered), "bytes")

    print()

    print("Integrity Check :", original == recovered)


if __name__ == "__main__":
    main()