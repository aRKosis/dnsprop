#!/bin/usr/env python

import sys, argparse


def cli_parser():
    parser = argparse.ArgumentParser(add_help=False, description=
        ''' 
        DNS proprogration is often a pain to track and maintain.\n
        It is often needed to to ensure that US wide that the current record is \n
        a simple yet effective way to get what Recon-Ng gets and theHarvester gets.\n\n
        Example Usage:\n
        Query all records in a loop: ./dnsprop -Q -D domain.com\n
        Query A records and compare for prop: ./dnsprop -D domain.com -A 104.1.1.1\n
        Query MX records and compare for prop: ./dnsprop -D domain.com -MX mail.domain.com\n
        (You may want to run -h)
        ''')
    parser.add_argument("-A", metavar='8.8.8.8', help="set A record you would like to check for.")
    parser.add_argument("-AAAA", metavar='8::::2', help="set A record you would like to check for.")
    parser.add_argument("-MX", metavar="smtp.target.com", help="set MX record you would like to check for.")
    parser.add_argument("-TXT", metavar="SPF: ~all ex.", help="set TXT record you would like to check for.")
    parser.add_argument("-SOA", metavar="")
    parser.add_argument("-Q", action='store_true', help="pure query for domain in loop")
    parser.add_argument("-D", metavar="domain.com", help="set domain to query dns for")
    parser.add_argument("-v", action='store_true', help="Set this switch for verbose output of modules")
    parser.add_argument('-h', '-?', '--h', '-help', '--help', action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
        
    if args.h:
        parser.print_help()
        sys.exit()
    return args.A, args.MX, args.Q, args.D, args.V

