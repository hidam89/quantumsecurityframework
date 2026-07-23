"""
benchmark_engine.py

Research-grade benchmarking engine.
"""

import time

from src.qsbf.benchmarking.benchmark_result import BenchmarkResult


class BenchmarkEngine:

    def benchmark_key_generation(self, algorithm, key_size):

        start = time.perf_counter()

        algorithm.generate_keys()

        end = time.perf_counter()

        return BenchmarkResult(
            algorithm=algorithm.name,
            key_size=key_size,

            key_generation_time=end - start,
            encryption_time=0.0,
            decryption_time=0.0,

            plaintext_size=0,
            ciphertext_size=0,

            memory_usage_mb=0.0,
            cpu_usage_percent=0.0,

            success=True
        )

    def benchmark_encryption(
        self,
        algorithm_name,
        key_size,
        encrypt_function,
        plaintext
    ):

        start = time.perf_counter()

        ciphertext = encrypt_function()

        end = time.perf_counter()

        return (
            ciphertext,
            BenchmarkResult(
                algorithm=algorithm_name,
                key_size=key_size,

                key_generation_time=0.0,
                encryption_time=end - start,
                decryption_time=0.0,

                plaintext_size=len(plaintext),
                ciphertext_size=len(ciphertext),

                memory_usage_mb=0.0,
                cpu_usage_percent=0.0,

                success=True
            )
        )

    def benchmark_decryption(
        self,
        algorithm_name,
        key_size,
        decrypt_function,
        ciphertext
    ):

        start = time.perf_counter()

        plaintext = decrypt_function()

        end = time.perf_counter()

        return (
            plaintext,
            BenchmarkResult(
                algorithm=algorithm_name,
                key_size=key_size,

                key_generation_time=0.0,
                encryption_time=0.0,
                decryption_time=end - start,

                plaintext_size=len(plaintext),
                ciphertext_size=len(ciphertext),

                memory_usage_mb=0.0,
                cpu_usage_percent=0.0,

                success=True
            )
        )