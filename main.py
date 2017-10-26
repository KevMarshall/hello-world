

import logging
import logging.config
import os
import json


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

    

    initLogging(useConfFile=True)
    log=logging.getLogger(__name__)
    print log
    log.info("Main Starting...")


    
