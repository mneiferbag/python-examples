import asyncio

# Asynchronous coroutine
async def worker():
    print("Worker coroutine started")
    await asyncio.sleep(3)  # Simulating an I/O-bound task
    print("Worker coroutine completed")

# Execute the coroutine within the event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(worker())
loop.close()

# Continue with other tasks in the main program
print("Main program continues")

