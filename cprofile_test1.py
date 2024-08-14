import cProfile
import asyncio
from task1 import find_divisors
async def main():
    for num in range(1_000_000, 20_000_001, 1_000_000):
        divisors = await find_divisors(num)
        print(f"Число: {num}, Делители: {divisors}")

if __name__ == "__main__":
    cProfile.run('asyncio.run(main())', sort='cumtime')