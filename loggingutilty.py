import logging



def getLogger():
    log = logging.getLogger("STRATA")
    log.addHandler(logging.FileHandler('Strata.log'))
    log.setLevel(logging.DEBUG)
    log.info("logging started")
    return log
