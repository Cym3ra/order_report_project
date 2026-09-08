import pandas as pd
import pytest

from order_report.validation import validate_data, validate_required_columns

def test_missing_required_column():
    data = pd.DataFrame(
        {
            "order_id": [1],
            "quantity": [2],
        }
    )

    with pytest.raises(ValueError):
        validate_required_columns(data)


def test_empty_data():
    data = pd.DataFrame()

    with pytest.raises(ValueError):
        validate_data(data)

