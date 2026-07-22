from dataclasses import dataclass, asdict, field
from datetime import datetime


@dataclass
class BenchmarkResult:
    algorithm: str
    key_size: int

    key_generation_time: float
    encryption_time: float
    decryption_time: float

    plaintext_size: int
    ciphertext_size: int

    memory_usage_mb: float
    cpu_usage_percent: float

    success: bool
    error_message: str = ""

    timestamp: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    def to_dict(self) -> dict:
        """Convert benchmark result to dictionary."""
        return asdict(self)