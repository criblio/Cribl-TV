import logging
import logging.handlers
import random
import time
from logging.handlers import SysLogHandler

logger = logging.getLogger('CriblSyslog')
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address=('CRIBL-URL-GOES-HERE',9514))
logger.addHandler(handler)

formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
messages = [
    'Foo!',
    'Test message from Python to Cribl Stream',
    'this is debug',
    'this is critical',
]

# Send 10 random log messages, then 50 INFO events, repeating until stopped (Ctrl+C)
while True:
    for _ in range(10):
        level = random.choice(levels)
        message = random.choice(messages)
        logger.log(level, message)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] sent {logging.getLevelName(level)}: {message}")
        time.sleep(.1)

    for _ in range(50):
        message = random.choice(messages)
        logger.log(logging.INFO, message)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] sent INFO: {message}")
        time.sleep(.1)

