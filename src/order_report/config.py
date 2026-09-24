from pathlib import Path
from dataclasses import dataclass
import logging

@dataclass(frozen=True)
class ReportConfig:
    """Dessa sökvägar används för att skapa rapporter"""
    input_path: Path = Path("data/orders.csv")
    output_path: Path = Path("output")


def configure_logging() -> None:
    """Konfigurerar logging centralt för hela programmet.
    """
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s"
    )