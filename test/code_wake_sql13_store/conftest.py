"""Pytest configuration / fixtures."""


import pytest
from code_wake.test.conftest import *

from code_wake_sql13_store import Sql13Store


@pytest.fixture
def store_params():
    return (["sqlite:///:memory:"], {})


@pytest.fixture
def store_cls():
    return Sql13Store


@pytest.fixture
def store_cleanup():
    return lambda store: None
