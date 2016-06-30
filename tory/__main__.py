import sys
import os
import pprint

# Hack to get the CWD until we build a real python package
sys.path.append(os.getcwd().split('tory')[0]+"tory/tory/")

import util
from util import AliasedArgumentParser, AliasedSubParsersAction

import inventory
import network
import cpu
import ram
import user

def parse_input():
    parser = AliasedArgumentParser(prog='PROG',
                                   usage="%(prog)s [OPTION] CMD...",
                                   prefix_chars="-")
    parser.register('action', 'parsers', AliasedSubParsersAction)

    # commands following tory keyword (e.g. 'tory disks ...')
    subparsers = parser.add_subparsers(title='commands',
                                       metavar='CMD',
                                       dest='command')
    # This is just a sample flag, it doesn't do anything yet.
    parser.add_argument('-m',
                        '--max-records',
                        action='store',
                        dest='max_records',
                        default=200,
                        help='Maximum number of records to show')
    
    # get disks
    sub_get_disks = subparsers.add_parser('disks',
                                              aliases=['disk'],
                                              help='Get info on disks')
    # get network
    sub_get_network = subparsers.add_parser('network',
                                              aliases=['net'],
                                              help='Get info on network')
    #get cpu
    sub_get_cpu = subparsers.add_parser('cpu', 
                                              aliases=['cpu'], 
                                              help='Get info on CPU')
    #get ramOS
    sub_get_ram = subparsers.add_parser('ram',
		    			      aliases=['ram'],
					      help='Get info on RAM')
    #get user
    sub_get_user = subparsers.add_parser('user',
                                              aliases=['users'],
                                              help='Get info on users')

    args = parser.parse_args()
    return args

def main():
    args = parse_input()
    if args.command == 'disks':
        pprint.pprint(inventory.get_disk_partitions())
    if args.command == 'network':
        pprint.pprint(network.get_network_info())
<<<<<<< HEAD
    if args.command == 'cpu':
        pprint.pprint(cpu.mch_cpu())
=======
    if args.command == 'ram':
	pprint.pprint(ram.get_ram_partitions())
<<<<<<< HEAD
>>>>>>> 18eab7d479a07d5bd71f883e9315bc8bd32c6c91
=======
    if args.command == 'user':
        pprint.pprint(user.get_users())
    if args.command == 'cpu':
        pprint.pprint(cpu.mch_cpu())
>>>>>>> 2b9367ada298322f87e966a978d23459e51a3bce

if __name__ == '__main__':
    main()
