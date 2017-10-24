


import logging
import os


def initLogging(logLevel=logging.DEBUG,logPath="logs/"):
    """
    Sets up the basic logging
    """

    logPath = os.path.join(logPath,"MainLog.log")
    logging.basicConfig(level=logLevel,
                        handlers=[logging.FileHandler(logPath),
                                  logging.StreamHandler()])

if __name__ == "__main__":

    initLogging()
    log=logging.getLogger()

    log.info('Starting %s'%__name__)
    
