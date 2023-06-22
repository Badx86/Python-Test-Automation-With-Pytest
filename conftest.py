from datetime import datetime, timedelta
from typing import Callable
from rest_framework.test import APIClient
import pytest
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.coronavstech.coronavstech.settings')
settings.configure()


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    diff = tock - tick
    print(f"\n runtime: {diff.total_seconds()}")


class PerformanceException(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_function_and_validate_runtime(*args, **kwargs):
        tick = datetime.now()
        result = method(*args, **kwargs)
        method(*args, **kwargs)
        tock = datetime.now()
        runtime = tock - tick
        print(f"\n runtime: {runtime.total_seconds()}")

        if runtime > runtime_limit:
            raise PerformanceException(runtime=runtime, limit=runtime_limit)
        return result

    return run_function_and_validate_runtime


@pytest.fixture
def api_client():
    return APIClient()
