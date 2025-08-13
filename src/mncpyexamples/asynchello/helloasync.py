"""Basic asyncio usage examples.

Copyright (c) 2025 Markus Neifer
Licensed under the MIT License.
See file LICENSE in project root directory.
"""
import asyncio

async def main():
    """Say hello asynchronously."""
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

def run_main():
    """Run the main asynchronous function."""
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())
