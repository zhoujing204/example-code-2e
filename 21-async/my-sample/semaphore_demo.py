import asyncio
import random
import time

async def print_semaphore_counter(value, semaphore):
    print(f"Starting task{value}...")
    async with semaphore:
        print(f"Semaphore counter: {semaphore._value}")
        # seconds = random.randint(0, 4)
        print(f'Task{value} will sleep for {value} seconds')
        time.sleep(value)        
    print("ending...\n")
    return value

async def main():
    semaphore = asyncio.Semaphore(value=3)
    
    to_do = [ print_semaphore_counter(i, semaphore) for i in range(5)]    
    to_do_iter = asyncio.as_completed(to_do)
    results = []
    for coro in to_do_iter:
        result = await coro
        results.append(result)
    print(f"Results: {results}")

asyncio.run(main())