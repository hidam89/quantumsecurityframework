"""
benchmark_engine.py

Core benchmarking engine for the Quantum Security Benchmarking Framework (QSBF).
"""

from src.qsbf.utils.timer import Timer
from src.qsbf.benchmarking.benchmark_result import BenchmarkResult


class BenchmarkEngine:
    """
    Executes benchmark operations on cryptographic algorithms.
    """

    def benchmark_key_generation(self, algorithm, key_size: int) -> BenchmarkResult:
        """
        Benchmark cryptographic key generation.

        Args:
            algorithm: Algorithm instance.
            key_size: Key size in bits.

        Returns:
            BenchmarkResult
        """

        with Timer() as timer:
            algorithm.generate_keys()

        return BenchmarkResult(
            algorithm=algorithm.name,
            key_size=key_size,
            key_generation_time=timer.elapsed,
            encryption_time=0.0,
            decryption_time=0.0,
            plaintext_size=0,
            ciphertext_size=0,
            memory_usage_mb=0.0,
            cpu_usage_percent=0.0,
            success=True,
        )