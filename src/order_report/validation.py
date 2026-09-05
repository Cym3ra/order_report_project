import pandas as pd

REQUIRED_COLUMNS = {
        "order_id",
        "order_date",
        "customer_id",
        "region",
        "product_category",
        "quantity",
        "unit_price",
        "discount",
        "returned",
        }


def validate_required_columns(data: pd.DataFrame) -> None:
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Obligatoriska kolumner saknas: {missing}")


def validate_data(data: pd.DataFrame) -> None:
    validate_required_columns(data)

    if data.empty:
        raise ValueError("Orderdata innehåller inga rader")