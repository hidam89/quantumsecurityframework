from src.qsbf.utils.logger import Logger
from src.qsbf.utils.timer import Timer


def main():

    logger = Logger()

    logger.info("Starting Timer Test")

    with Timer() as timer:

        total = 0

        for i in range(1_000_000):

            total += i

    logger.info(f"Execution Time : {timer.elapsed:.6f} seconds")


if __name__ == "__main__":
    main()