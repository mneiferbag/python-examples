import asyncio
from loguru import logger

from logger1 import Logger1
from logger2 import Logger2
from logger3 import Logger3
from csvwriter import CSVWriter

async def main(csvwriter):
    logger1 = Logger1("Logger1", csvwriter)
    logger2 = Logger2("Logger2", csvwriter)
    logger3 = Logger3("Logger3", csvwriter)

    await asyncio.gather(
        logger1.connect(),
        logger2.connect(),
        logger3.connect()
    )

if __name__ == '__main__':
    csvwriter = CSVWriter('output.csv')
    csvwriter.open()

    try:
        asyncio.run(main(csvwriter))
    except KeyboardInterrupt:
        logger.info("Received KeyboardInterrupt. Shutting down...")

    csvwriter.close()
