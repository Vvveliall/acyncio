import asyncio
import cProfile
from task1 import find_divisors
import pytest

@pytest.mark.asyncio
async def test_find_divisors():
    assert await find_divisors(1) == [1]
    assert await find_divisors(6) == [1, 2, 3, 6]
    assert await find_divisors(12) == [1, 2, 3, 4, 6, 12]
    assert await find_divisors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert await find_divisors(1_000_000) == [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000, 2000, 2500, 5000, 10000, 12500, 25000, 50000, 100000, 125000, 250000, 500000, 1000000]


