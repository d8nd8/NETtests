import pytest
from task2 import check_email


@pytest.mark.parametrize(
    'email,expected',
    (
            ("netologiyarulitro.ru", False),
            ("jumppmuj@yandex.ru", True),
            ("el mail@mail.com", True),
    )
)
def test_check1_with_params(email, expected):
    result = check_email(email)
    assert result == expected
