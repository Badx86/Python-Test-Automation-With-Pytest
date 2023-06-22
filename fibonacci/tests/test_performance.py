import pytest
from fibonacci.dynamic import fibonacci_dynamic_v2
from conftest import track_performance


@pytest.mark.performance
@track_performance
def test_performance():
    fibonacci_dynamic_v2(1000)


@pytest.mark.performance
def test_performance_under_load():
    for _ in range(2000):
        @track_performance
        def run_test():
            fibonacci_dynamic_v2(1000)

        run_test()
