import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

def load_orders(path: Path) -> pd.DataFrame:
    """Läser orderdata från en CSV-fil.
    """
    
    if not path.exists():
        raise FileNotFoundError(f"Hittar inte datafilen: {path}")
    
    logger.info("Läser orderdata från %s", path)

    data = pd.read_csv(path)
    
    logger.info("Läste in %d rader", len(data))

    return data