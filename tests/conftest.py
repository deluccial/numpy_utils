import pytest
import numpy as np


@pytest.fixture
def arr() -> np.ndarray:
    return np.array([[1, 1], [-1, 0]])


@pytest.fixture
def arr_alt() -> np.ndarray:
    return np.array([[1, 1, 1], [-1, 0, 0], [1, 1, 1]])
