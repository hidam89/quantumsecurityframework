from src.qsbf.benchmarking.benchmark_engine import BenchmarkEngine
from src.qsbf.rsa.rsa_algorithm import RSAAlgorithm


def main():

    engine = BenchmarkEngine()

    rsa = RSAAlgorithm()

    result = engine.benchmark_key_generation(
        rsa,
        2048
    )

    print(result)

    print()

    print(result.to_dict())


if __name__ == "__main__":

    main()