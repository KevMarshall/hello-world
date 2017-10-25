

import logging
import os

import module


def initLogging(logLevel=logging.DEBUG,logPath="logs/"):
    """
    Sets up the basic logging
    """

    logPath = os.path.join(logPath,"MainLog.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(logPath)
    fh.setLevel(logLevel)
    fh.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setLevel(logLevel)
    ch.setFormatter(formatter)
    l = logging.getLogger()
    l.addHandler(ch)
    l.addHandler(fh)
    l.setLevel(logLevel)

if __name__ == "__main__":

    initLogging()
    log=logging.getLogger(__name__)


    
