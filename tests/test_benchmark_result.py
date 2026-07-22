from src.qsbf.benchmarking.benchmark_result import BenchmarkResult


def main():

    result = BenchmarkResult(

        algorithm="RSA",

        key_size=2048,

        key_generation_time=0.023,

        encryption_time=0.001,

        decryption_time=0.0012,

        plaintext_size=1024,

        ciphertext_size=256,

        memory_usage_mb=12.5,

        cpu_usage_percent=4.6,

        success=True

    )

    print(result)

    print()

    print(result.to_dict())


if __name__ == "__main__":

    main()
