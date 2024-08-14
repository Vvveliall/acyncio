#Дано число в диапазоне от 1_000_000 до 20_000_000. Получите список целочисленных делителей этого числа.

import asyncio

async def find_divisors(num):
    """
    Функция, которая находит все целочисленные делители заданного числа.
    """
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sorted(divisors)

async def main():
    """
    Основная функция, которая запускает поиск делителей для числа в диапазоне.
    """
    for num in range(1_000_000, 20_000_001, 1_000_000):
        divisors = await find_divisors(num)
        print(f"Число: {num}, Делители: {divisors}")

if __name__ == "__main__":
    asyncio.run(main())
