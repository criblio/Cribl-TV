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

# Send one random log message every second until stopped (Ctrl+C)
while True:
    level = random.choice(levels)
    message = random.choice(messages)
    logger.log(level, message)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] sent {logging.getLevelName(level)}: {message}")
    time.sleep(1)

