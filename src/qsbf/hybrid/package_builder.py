"""
package_builder.py

Builds Hybrid Encryption Packages.
"""

import pickle


class HybridPackageBuilder:
    """
    Builds a serialized hybrid encryption package.
    """

    def build(
        self,
        metadata,
        nonce,
        encrypted_key,
        ciphertext,
    ):

        package = {
            "metadata": metadata,
            "nonce": nonce,
            "encrypted_key": encrypted_key,
            "ciphertext": ciphertext,
        }

        return pickle.dumps(package)