import asyncio
from loguru import logger

async def main():
    logger.info('Starting asyncio example')
    await asyncio.sleep(1)
    logger.success('Asyncio example finished')

async def main2():
    logger.info('Starting second asyncio example')
    await asyncio.sleep(1)
    logger.success('Second asyncio example finished')

if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(main2())
