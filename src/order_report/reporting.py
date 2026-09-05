
from pathlib import Path
import pandas as pd






def save_report(report: pd.DataFrame, path: Path, filename: str) -> None:
    """Spara rapport som en CSV fil"""

    path.parent.mkdir(parents=True, exist_ok=True)
    output_path = path / filename
    report.to_csv(output_path, index=False)