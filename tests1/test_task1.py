import pytest
from task1 import check_auth


@pytest.mark.parametrize(
    'login,password,expected',
    (
            ("admin", "password", "Добро пожаловать"),
            ("vasya", "vasin", "Доступ ограничен"),
            ("amd1n", "password", "Доступ разрешен"),
    )
)
def test_check1_with_params(login, password, expected):
    result = check_auth(login, password)
    assert result == expected
