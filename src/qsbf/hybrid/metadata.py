from dataclasses import dataclass


@dataclass
class HybridMetadata:

    version: str

    algorithm: str

    rsa_key_size: int

    aes_key_size: int

    nonce_length: int

    encrypted_key_length: int

    ciphertext_length: int