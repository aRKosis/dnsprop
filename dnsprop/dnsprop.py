#!/bin/usr/env python

"""
  The main controller class for DNSPropagation Checker.

  This will launch from ./dnsprop

"""

import sys, argparse, os
import dns.resolver
import dns.query

# local imports

from lib import dnsresolver
from lib import parsing




def cli_parser():
    parser = argparse.ArgumentParser(prog='dnsprop', conflict_handler = 'resolve', add_help=False, description=
        ''' 
        DNS proprogration is often a pain to track and maintain.\n
        It is often needed to to ensure that US wide that the current record is
        a simple yet effective way to get what Recon-Ng gets and theHarvester gets
        ''')

                                                    #required arguments

    parser.add_argument('addr', 
                        help='DNS server IP address you wish to check.')

    parser.add_argument('domain', 
                        help='Your domain.')

                                                    #positional arguments

    parser.add_argument('-h', '--help', '-H',
                        action="store_true", 
                        help=argparse.SUPPRESS)

    parser.add_argument('-f', '--file',
                        metavar='filepath', 
                        help='Filepath to IPlist you wish to check for propogation.', 
                        nargs='+')

    parser.add_argument("-A", 
                        metavar='8.8.8.8', 
                        help="check for A record (IPv4)")

    parser.add_argument("-AAAA", 
                        metavar='8::::2', 
                        help="check for AAAA record (IPv6).")

    parser.add_argument("-MX", 
                        metavar="ex.tar.com", 
                        help="Check for MX record.")

    parser.add_argument("-TXT", 
                        metavar="SPF: ~all ex.", 
                        help="Set TXT record you would like to check for.")

    parser.add_argument("-SOA", 
                        metavar="")

    parser.add_argument("-Q", '--query',
                        help="Pure query for domain in loop")

    parser.add_argument("-D", 
                        metavar="domain.com", 
                        help="Set domain to query dns for")

    parser.add_argument("-V", '--verbose',
                        action='store_true', 
                        help="Set this switch for verbose output of modules.")

    parser.add_argument('-o','--output', 
                        metavar='Filepath/Name', 
                        help='Writes output to specified file.')


    args = parser.parse_args()
      

    if args.h:
        parser.print_help()
        sys.exit()

    return args.h, args.A, args.MX, args.Q, args.D, args.V, args.addr, args.domain, args.f, args.SOA, args.TXT


def dns_propogation(variable):

    try:
        if args.addr != '':
            dnsresolver()

    except Exception as e:
        print (e)

    return 0


def main():

    resolve = dnsresolver.dnsresolver()
    
    dns_propogation(resolve)



if __name__ == "__main__":
  try:  
    main()
  except KeyboardInterrupt:
    print 'Interrupted'
  try:
    sys.exit(0)
  except SystemExit:
    os._exit(0)