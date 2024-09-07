from task3 import get_cost
import pytest

@pytest.mark.parametrize(
    'weight,expected',
    (
            (3, "Стоимость доставки: 200 руб."),
            (4, "Стоимость доставки: 500 руб."),
            (240, "Стоимость доставки: 500 руб."),
    )
)
def test_check1_with_params(weight, expected):
    result = get_cost(weight)
    assert result == expected
