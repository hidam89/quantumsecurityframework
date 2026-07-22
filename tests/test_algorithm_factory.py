from src.qsbf.core.algorithm_factory import AlgorithmFactory
from src.qsbf.rsa.rsa_algorithm import RSAAlgorithm

AlgorithmFactory.register("RSA", RSAAlgorithm)

algorithm = AlgorithmFactory.create("RSA")

print(algorithm.name)

algorithm.initialize()