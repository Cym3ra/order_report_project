import pandas as pd
import logging

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

logger = logging.getLogger(__name__)

def validate_required_columns(data: pd.DataFrame) -> None:
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Obligatoriska kolumner saknas: {missing}")


def validate_data(data: pd.DataFrame) -> None:
    #validate_required_columns(data)

    if data.empty:
        raise ValueError("Orderdata innehåller inga rader")



def validate_orders(data: pd.DataFrame) -> list[str]:
    errors: list[str] = []

    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        errors.append(
            "Saknade kolumner: "
            + ", ".join(sorted(missing_columns))
        )

    if data.empty:
        errors.append(
            "Datafilen innehåller inga rader."
        )

    if missing_columns:
        return errors

    if data["order_id"].isna().any():
        errors.append(
            "Kolumnen order_id innehåller tomma värden."
        )

    for column in ["quantity", "unit_price", "discount"]:
        try:
            values = pd.to_numeric(
                data[column],
                errors="raise",
            )

            if (values < 0).any():
                errors.append(
                    f"Kolumnen {column} innehåller "
                    "negativa värden."
                )

        except (ValueError, TypeError):
            errors.append(
                f"Kolumnen {column} måste innehålla tal."
            )

    return errors