from src.qsbf.benchmarking.benchmark_engine import BenchmarkEngine

from src.qsbf.rsa.key_generator import RSAKeyGenerator
from src.qsbf.rsa.encryptor import RSAEncryptor
from src.qsbf.rsa.decryptor import RSADecryptor


def main():

    generator = RSAKeyGenerator(2048)

    private_key, public_key = generator.generate()

    plaintext = b"Quantum Security Benchmark Framework"

    encryptor = RSAEncryptor()

    decryptor = RSADecryptor()

    engine = BenchmarkEngine()

    ciphertext, enc_result = engine.benchmark_encryption(
        "RSA",
        2048,
        lambda: encryptor.encrypt(public_key, plaintext),
        plaintext
    )

    recovered, dec_result = engine.benchmark_decryption(
        "RSA",
        2048,
        lambda: decryptor.decrypt(private_key, ciphertext),
        ciphertext
    )

    print("=" * 60)

    print(enc_result)

    print()

    print(dec_result)

    print()

    print("Integrity:", recovered == plaintext)


if __name__ == "__main__":
    main()