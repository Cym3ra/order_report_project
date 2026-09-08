
from pathlib import Path
import pandas as pd
import logging

from .processing import (
    calculate_order_values,
    order_overview,
    summarise_data,
    returns_summary,
    sort_by_sales
)

logger = logging.getLogger(__name__)

def save_report(report: pd.DataFrame, path: Path, filename: str) -> None:
    """Spara rapport som en CSV fil"""

    path.parent.mkdir(parents=True, exist_ok=True)
    output_path = path / filename
    report.to_csv(output_path, index=False)

def build_reports(report_data: pd.DataFrame) -> dict[str, pd.DataFrame]:
    data = calculate_order_values(report_data)

    overview = order_overview(data)

    sales_by_category = sort_by_sales(summarise_data(data, "product_category"))
    sales_by_region = sort_by_sales(summarise_data(data, "region"))
    returns_by_category = returns_summary(summarise_data(data, "product_category"), "product_category")

    logger.info("Byggde rapporter för: overview, sales_by_category, sales_by_region, returns_by_category")

    return {
        "overview.csv": overview,
        "sales_by_category.csv": sales_by_category,
        "sales_by_region": sales_by_region,
        "returns_by_category": returns_by_category,
    }


def create_reports(report_data: pd.DataFrame, output_dir:Path):
    reports = build_reports(report_data)
    for filename, report in reports.items():
        save_report(report, output_dir / filename)
        return reports
    logger.info("Sparade rapport till %s", output_dir)