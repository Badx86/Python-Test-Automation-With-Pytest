import pytest
from django.urls import reverse
from fibonacci.dynamic import fibonacci_dynamic, fibonacci_dynamic_v2
from typing import Callable
from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
from fibonacci.naive import fibonacci_naive


@pytest.mark.parametrize(
    "fib_func",
    [
        fibonacci_naive,
        fibonacci_cached,
        fibonacci_lru_cached,
        fibonacci_dynamic,
        fibonacci_dynamic_v2,
    ],
)
@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fibonacci(
        time_tracker, fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    res = fib_func(n)
    assert res == expected


@pytest.mark.parametrize(
    "n,expected,expected_status_code",
    [
        (0, {'fibonacci': 0}, 200),
        (1, {'fibonacci': 1}, 200),
        (2, {'fibonacci': 1}, 200),
        (9, {'fibonacci': 34}, 200),
        ('abc', {'error': 'n must be an integer'}, 400),
        (-5, {'error': 'n must be non-negative'}, 400)
    ]
)
def test_fibonacci_endpoint(api_client, n, expected, expected_status_code):
    response = api_client.get(reverse('get_fibonacci'), {'n': n})
    assert response.status_code == expected_status_code
    assert response.json() == expected
