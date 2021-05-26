import os
import sys
import time
import logging


# logger related
def get_logger():
    LOG_FORMAT = "%(asctime)s %(name)s - %(levelname)7s: %(message)s"
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO,
                        format=LOG_FORMAT,
                        datefmt="%m/%d %I:%M:%S %p")
    logger = logging.getLogger("OGLE")

    # file handler
    filename = time.strftime('OGLE-%m.%d-%H.%M.%S.txt', time.localtime(time.time()))
    log_path = os.path.join("logs", filename)
    fh = logging.FileHandler(log_path, mode='w')
    fh.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(fh)

    return logger


def prompt(text, n=20):
    return "=" * n + text + "=" * n
