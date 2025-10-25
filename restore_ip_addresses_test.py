import pytest
import restore_ip_addresses as test


def test_get_valid_ips():
    response = test.get_valid_ips("0000")
    assert response == ["0.0.0.0"]

    response = test.get_valid_ips("25525511135")
    assert response == ["255.255.11.135", "255.255.111.35"]

    response = test.get_valid_ips("101023")
    assert response == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]


@pytest.mark.parametrize(
    "ip,expected",
    [
        ("", False),
        ("x", False),
        ("1.1.1.x", False),
        ("1.1.1.1", True),
    ],
)
def test_is_valid_ip(ip, expected):
    assert test.is_valid_ip(ip) == expected


@pytest.mark.parametrize(
    "number,expected",
    [
        ("-1", False),
        ("0", True),
        ("1", True),
        ("01", False),
        ("100", True),
        ("254", True),
        ("255", True),
        ("256", False),
        ("1000", False),
    ],
)
def test_is_valid_octet(number, expected):
    assert test.is_valid_octet(number) == expected


@pytest.mark.parametrize(
    "string_length,expected",
    [
        (4, [[1, 1, 1]]),
        (5, [[1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1]]),
    ],
)
def test_get_possible_period_indexes(string_length, expected):
    assert test.get_possible_period_indexes(string_length) == expected
