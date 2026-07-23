"""
package_parser.py

Parses Hybrid Encryption Packages.
"""

import pickle


class HybridPackageParser:
    """
    Parses serialized hybrid encryption packages.
    """

    def parse(self, package_bytes):

        package = pickle.loads(package_bytes)

        return (
            package["metadata"],
            package["nonce"],
            package["encrypted_key"],
            package["ciphertext"],
        )