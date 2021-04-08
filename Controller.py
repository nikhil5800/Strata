import requests
import traceback
from Datalayer import *
import loggingutilty
class Manage:
    def __init__(self,args):
        self.log = loggingutilty.getLogger()
        self.argslist = args

    def getresponse(self):
        try:
            if self.argslist.get('UserName'):
                self.log.info('Username %s',self.argslist.get('UserName'))
                return Network().search(self.argslist.get('UserName'))
            elif self.argslist.get('Filter'):
                self.log.info('Filter %s', self.argslist.get('Filter'))
                return Network().filter(self.argslist.get('Filter'))

            elif self.argslist.get('Create'):
                self.log.info('create %s', self.argslist.get('create'))
                return Network().create(self.argslist.get('create'))
            else:
                return {'ERROR':'no valid input {0}'.format(self.argslist)}
        except:
            self.log.info('ERROR %s', traceback.format_exc())

            return {'ERROR':traceback.format_exc()}





