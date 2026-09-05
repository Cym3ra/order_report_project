from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class ReportConfig:
    """Dessa sökvägar används för att skapa rapporter"""
    input_path: Path = Path("data/orders.csv")
    output_path: Path = Path("output")