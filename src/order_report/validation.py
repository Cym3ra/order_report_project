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


def validate_orders(data: pd.DataFrame) -> list[str]:
    """Kör samtliga kontroller och samlar eventuella fel i en lista."""
    errors: list[str] = []

    missing_columns = REQUIRED_COLUMNS.difference(data.columns)

    if missing_columns:
        errors.append("Saknade kolumner: " + ", ".join(sorted(missing_columns)))

    if data.empty:
        errors.append("Datafilen innehåller inga rader.")

    if missing_columns:
        return errors

    if data["order_id"].isna().any():
        errors.append("Kolumnen order_id innehåller tomma värden.")

    for column in ["quantity", "unit_price", "discount"]:
        values = pd.to_numeric(data[column], errors="coerce")

        if (values < 0).any():
            errors.append(f"Kolumnen {column} innehåller negativa värden.")

    return errors