import argparse
import json
import Controller
import loggingutilty as log
my_parser = argparse.ArgumentParser(description='Take User inputs for various API calls')
# group = my_parser.add_mutually_exclusive_group()
# group.add_argument('-u','--UserName', help='to get info about the entity matching user name',action='store_true')
# group.add_argument('--Filter', help = 'look for a particular entity', action='store_false')

my_parser.add_argument("--UserName", help='to get info about the entity matching user name')
my_parser.add_argument("--Filter", help = 'look for a particular entity')



my_parser.add_argument("--Create", help='Create an Entity based on userinputs', type = json.loads)



args_parse = my_parser.parse_args()
log.getLogger().info('response is %s',Controller.Manage(vars(args_parse)).getresponse())



