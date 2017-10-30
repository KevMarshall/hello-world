

import logging
import logging.config
import os
import argparse
import json


def getArgs():

    args = argparse.ArgumentParser(description="This is a Kevin Marshall Production")
    args.add_argument('-c', dest='configMode',default='default', action="store", choices=['default','file'])
    args.add_argument('-log-path', dest='logPath',default=None)
    argVals = args.parse_args()

    return argVals
    

def initLogging(useConfFile = False, logLevel=logging.DEBUG,logPath="logs/"):
    """
    Sets up the basic logging
    """

    if useConfFile:

        logConfPath = 'cfg/loggingConfig.json'

        if os.path.exists(logConfPath):
            
            with open(logConfPath,'rt') as cnfFile:
                config = json.load(cnfFile)

            logging.config.dictConfig(config)
                

    else:
        
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

    """
    Get the command line options and unpack them
    """
    argVals = getArgs()

    configMode = argVals.configMode
    logPath = argVals.logPath

    """
    Set up the logging
    """    
    initLogging(useConfFile=True)
    log=logging.getLogger(__name__)

    log.info("Main Starting...")
    log.info("Config mode is %s" %configMode)
    log.info("logPath is %s" %logPath)


    
