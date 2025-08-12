import asyncio
import time

async def nested():
    for i in range(1000):
        print(42)

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    print("Task started...")
    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    #await task
    time.sleep(5)
    task.cancel()

asyncio.run(main())

