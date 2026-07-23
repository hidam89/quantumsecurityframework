from src.qsbf.benchmarking.benchmark_result import BenchmarkResult
from src.qsbf.reports.csv_exporter import CSVExporter


def main():

    result = BenchmarkResult(

        algorithm="RSA",

        key_size=2048,

        key_generation_time=0.021,

        encryption_time=0.001,

        decryption_time=0.001,

        plaintext_size=64,

        ciphertext_size=256,

        memory_usage_mb=15,

        cpu_usage_percent=3,

        success=True,
    )

    exporter = CSVExporter()

    exporter.export(
        "rsa_results.csv",
        result,
    )

    print("CSV exported successfully.")


if __name__ == "__main__":

    main()