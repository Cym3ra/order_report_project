import pandas as pd

from order_report.processing import calculate_order_values, order_overview

def test_calculate_order_values():
    data = pd.DataFrame(
        {
            "quantity": [2],
            "unit_price": [100],
            "discount": [0.10],
        }
    )

    result = calculate_order_values(data)

    assert result["order_value"].iloc[0] == 200
    assert result["discounted_value"].iloc[0] == 180


def test_calculate_multiple_order_values():
    data = pd.DataFrame(
        {
            "quantity": [2, 3],
            "unit_price": [100, 50],
            "discount": [0.10, 0],
        }
    )

    result = calculate_order_values(data)

    assert result["order_value"].tolist() == [200, 150,]
    assert result["discounted_value"].tolist() == [180, 150,]


def test_order_overview():
    data = pd.DataFrame(
        {
            "order_id": [1, 2],
            "discounted_value": [100, 200],
            "returned": [False, True],
        }
    )

    result = order_overview(data)

    assert result.loc[0, "metric"] == "total_sales"
    assert result.loc[0, "value"] == 300

    assert result.loc[1, "metric"] == "order_count"
    assert result.loc[1, "value"] == 2

    assert result.loc[2, "metric"] == "return_count"
    assert result.loc[2, "value"] == 1