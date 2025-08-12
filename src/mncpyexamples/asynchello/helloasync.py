import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

def run_main():
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())
