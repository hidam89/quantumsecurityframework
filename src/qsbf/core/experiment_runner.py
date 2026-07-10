from src.qsbf.config.config_loader import ConfigLoader
from src.qsbf.utils.logger import Logger
from src.qsbf.utils.timer import Timer
from src.qsbf.utils.system_info import SystemInfo


class ExperimentRunner:
    """
    Quantum Security Benchmarking Framework
    Experiment Runner

    Responsibilities:
    - Load configuration
    - Initialize logger
    - Collect system information
    - Execute experiment
    - Record execution time

    Cryptographic algorithms (RSA, AES, PQC, etc.)
    are plugged into this runner.
    """

    def __init__(self):

        self.logger = Logger()
        self.config = ConfigLoader()
        self.system_info = SystemInfo()

    def show_header(self):

        self.logger.info("=" * 70)
        self.logger.info("Quantum Security Benchmarking Framework (QSBF)")
        self.logger.info("=" * 70)

    def load_configuration(self):

        self.logger.info("Loading configuration...")

        self.algorithm = self.config.get("algorithm")
        self.iterations = self.config.get("iterations")
        self.key_sizes = self.config.get("key_sizes")

        self.logger.info(f"Algorithm  : {self.algorithm}")
        self.logger.info(f"Iterations : {self.iterations}")
        self.logger.info(f"Key Sizes  : {self.key_sizes}")

    def collect_system_information(self):

        self.logger.info("Collecting system information...")

        info = self.system_info.save()

        self.logger.info(f"Processor        : {info['processor']}")
        self.logger.info(f"Operating System : {info['operating_system']}")
        self.logger.info(f"Physical Cores   : {info['physical_cores']}")
        self.logger.info(f"Logical Cores    : {info['logical_cores']}")
        self.logger.info(f"RAM              : {info['total_ram_gb']} GB")

    def execute_algorithm(self):

        """
        Placeholder.

        Later we will call:

            RSA Benchmark
            AES Benchmark
            Hybrid Benchmark
            ML-KEM Benchmark
            ML-DSA Benchmark
            OpenFHE Benchmark

        based on config.json
        """

        self.logger.info("No algorithm has been implemented yet.")

    def run(self):

        self.show_header()

        self.load_configuration()

        self.collect_system_information()

        self.logger.info("Starting Experiment...")

        with Timer() as timer:

            self.execute_algorithm()

        self.logger.info(
            f"Total Framework Time : {timer.elapsed:.6f} seconds"
        )

        self.logger.info("Experiment Finished Successfully")

        self.logger.info("=" * 70)