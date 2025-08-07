import asyncio
import random
from loguru import logger


class Logger1:
    def __init__(self, name, csvwriter):
        self.name = name
        self.csvwriter = csvwriter

    async def connect(self):
        logger.info(f"{self.name} is connecting...")
        await asyncio.sleep(1)
        logger.info(f"{self.name} connected successfully!")

        try:
            while True:
                logger.info(f"{self.name} is listening for events...")
                number = random.randint(1, 10)
                await asyncio.sleep(number)
                self.csvwriter.write("column2", number)
                self.csvwriter.flush()
        except KeyboardInterrupt:
            logger.info(f"{self.name} received KeyboardInterrupt. Shutting down...")
