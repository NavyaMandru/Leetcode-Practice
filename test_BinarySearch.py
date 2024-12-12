import pytest
from BinarySearch import binary_search


def test_binary_search():
    assert binary_search([1, 2, 3, 4], 4) == 3
