import asyncio
import http.client

# Максимальное количество одновременных запросов
MAX_CONCURRENT_REQUESTS = 10

async def send_request():
    conn = http.client.HTTPConnection("google.com")
    conn.request("GET", "/")
    response = conn.getresponse()
    print(f"Получен ответ с кодом {response.status}")

async def throttled_requests():
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    while True:
        async with semaphore:
            await send_request()

async def main():
    await asyncio.gather(
        *[throttled_requests() for _ in range(100)]
    )

if __name__ == "__main__":
    asyncio.run(main())