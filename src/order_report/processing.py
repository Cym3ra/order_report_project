import pandas as pd

def clean_order_data(data: pd.DataFrame) -> pd.DataFrame:

    clean_data = data.copy()

    clean_data["region"] = clean_data["region"].fillna("Unknown").astype(str).str.strip().str.title()
    clean_data["product_category"] = (
        clean_data["product_category"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    clean_data["quantity"] = pd.to_numeric(
        clean_data["quantity"], errors="coerce"
    ).fillna(1)

    clean_data["unit_price"] = pd.to_numeric(
        clean_data["unit_price"], errors="coerce"
    )
    clean_data["unit_price"] = clean_data["unit_price"].fillna(
        clean_data["unit_price"].median()
    )

    clean_data["discount"] = pd.to_numeric(
        clean_data["discount"], errors="coerce"
    ).fillna(0)

    clean_data["returned"] = (
        data["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )
    return clean_data


def calculate_order_values(data: pd.DataFrame) -> pd.DataFrame:

    result = data.copy()

    result["order_value"] = (
        result["quantity"] * result["unit_price"]
    )
    
    result["discounted_value"] = (
        result["order_value"] * (1 - result["discount"])
    )
    return result

def order_overview(data: pd.DataFrame) -> pd.DataFrame:
    total_sales = round(float(data["discounted_value"].sum()), 2,)
    
    number_of_orders = int(data["order_id"].nunique())
    number_of_returns = int(data["returned"].sum())

    return pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )

def summarise_data(data: pd.DataFrame, group_column: str) -> pd.DataFrame:
    summary = data.groupby(group_column, as_index=False,).agg(
        order_count=("order_id", "nunique"),
        total_sales=("discounted_value", "sum"),
        returns=("returned", "sum",)
    )
    summary["total_sales"] = summary["total_sales"].round(2)
    summary["return_rate"] = (summary["returns"] / summary["order_count"]).round(3)
    return (summary.sort_values("total_sales", ascending=False,).reset_index(drop=True))

def returns_summary(data: pd.DataFrame, group_column: str) -> pd.DataFrame:
    result = (data.groupby("product_category", as_index=False,).agg
              (order_count=("order_id", "nunique"),
                returns=("returned", "sum"),)
            )
    result["return_rate"] = (
        result["returns"] / result["order_count"]
    ).round(3)

    return (result.sort_values("return_rate", ascending=False,).reset_index(drop=True))