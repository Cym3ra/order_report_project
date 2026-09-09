import pandas as pd
import pytest

from order_report.validation import validate_orders


REQUIRED_DATA = {
    "order_id": ["O0001"],
    "order_date": ["2026-01-04"],
    "customer_id": ["C018"],
    "region": ["North"],
    "product_category": ["Electronics"],
    "quantity": [2],
    "unit_price": [499],
    "discount": [0.1],
    "returned": [False],
}


def test_validate_orders_with_valid_data():
    data = pd.DataFrame(REQUIRED_DATA)

    errors = validate_orders(data)

    assert errors == []


def test_validate_orders_detects_missing_column():
    data = pd.DataFrame(REQUIRED_DATA)
    data = data.drop(columns=["region"])

    errors = validate_orders(data)

    assert errors == ["Saknade kolumner: region"]


def test_validate_orders_detects_empty_data():
    data = pd.DataFrame(columns=REQUIRED_DATA.keys())

    errors = validate_orders(data)

    assert "Datafilen innehåller inga rader." in errors


def test_validate_orders_detects_missing_order_id():
    data = pd.DataFrame(REQUIRED_DATA)
    data.loc[0, "order_id"] = None

    errors = validate_orders(data)

    assert "Kolumnen order_id innehåller tomma värden." in errors


def test_validate_orders_detects_negative_value():
    data = pd.DataFrame(REQUIRED_DATA)
    data.loc[0, "quantity"] = -2

    errors = validate_orders(data)

    assert "Kolumnen quantity innehåller negativa värden." in errors

