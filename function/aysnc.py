# in this file, we compare the diff between async and sync execution of multiple requests
# async means no-blocking, so it can execute multiple requests at the same time
# sync means blocking, so it can only execute one request at a time
# NOTE: the async doesn't mean the multi-threading, it's single-threaded to mange multiple tasks concurrently
import asyncio
import time
from aiohttp import ClientSession

# Asynchronous function to fetch a URL
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

# Asynchronous test with `async def`
async def test_async(urls):
    async with ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Synchronous test without `async def`
def test_sync(urls):
    import requests
    results = []
    for url in urls:
        response = requests.get(url)
        results.append(response.text)
    return results

# Main function to compare
def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts/1"
    ]

    # Test async execution
    start_time = time.time()
    asyncio.run(test_async(urls))
    print(f"Async Execution Time: {time.time() - start_time:.2f} seconds")

    # Test sync execution
    start_time = time.time()
    test_sync(urls)
    print(f"Sync Execution Time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()