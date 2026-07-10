from src.qsbf.config.config_loader import ConfigLoader
from src.qsbf.utils.logger import Logger
from src.qsbf.utils.timer import Timer


class ExperimentRunner:

    def __init__(self):

        self.logger = Logger()
        self.config = ConfigLoader()

    def run(self):

        self.logger.info("=" * 60)
        self.logger.info("Quantum Security Benchmarking Framework")
        self.logger.info("=" * 60)

        self.logger.info(
            f"Algorithm : {self.config.get('algorithm')}"
        )

        self.logger.info(
            f"Iterations : {self.config.get('iterations')}"
        )

        self.logger.info("Starting benchmark...")

        with Timer() as timer:

            # Placeholder for future algorithms
            pass

        self.logger.info(
            f"Framework Execution Time : {timer.elapsed:.6f} seconds"
        )

        self.logger.info("Experiment Completed Successfully")