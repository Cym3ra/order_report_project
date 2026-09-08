import pandas as pd

from order_report.processing import calculate_order_values

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

