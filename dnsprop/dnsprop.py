#!/bin/usr/env python

"""
  The main controller class for DNSPropagation Checker. Yay!

  This will launch from ./dnsprop

"""

import sys, argparse, os
import dns.resolver
import dns.query

# local imports

from lib import dnsresolver
from lib import parsing

resolve = dnsresolver.dnsresolver()


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
                        action='store_true',
                        help=argparse.SUPPRESS)

    parser.add_argument("-A", '-a', 
                        action='store_true',
                        help="check for A record (IPv4)")

    parser.add_argument("-AAAA", '-aaaa',
                        action='store_true', 
                        help="check for AAAA record (IPv6).")

    parser.add_argument("-MX", '-mx',
                        action='store_true', 
                        help="Get MX record of domain.")

    parser.add_argument("-TXT", '-txt',
                        action='store_true', 
                        help="Get TXT record of domain.")

    parser.add_argument("-SOA", '-soa',
                        action='store_true',
                        help='Get SOA record of domain.')

    parser.add_argument("-NS", "-ns",
                        action='store_true',
                        help='Get NS record of domain.')

    parser.add_argument('-CNAME', '-cname',
                        action='store_true',
                        help='Get CNAME record of domain.')

    parser.add_argument('-DHCID', '-dhcid',
                        action='store_true',
                        help='Get DHCID record of domain.')

    # TODO
    # parser.add_argument("-Q", '--query', '-q',
    #                     help="Pure query for domain in loop")

    parser.add_argument("-V", '--verbose', '-v',
                        action='store_true', 
                        help="Set this switch for verbose output of modules.")

    parser.add_argument('-f', '--file', '-F',
                        metavar='filepath', 
                        help='Filepath to IPlist you wish to check for propogation.', 
                        nargs='+')

    parser.add_argument('-o','--output', '-O',
                        metavar='Filepath/Name', 
                        help='Writes output to specified file.',
                        nargs='+')


    args = parser.parse_args()

    if args.help:
        parser.print_help()
        sys.exit()

    return  args.addr, args.domain, args.help, args.A, args.AAAA, args.MX, args.SOA, args.TXT, args.NS, args.CNAME, args.DHCID, args.verbose, args.file, args.output


def dns_propogation():

    _addr, _domain, _help, _A, _AAAA, _MX, _SOA, _TXT, _NS, _CNAME, _DHCID, _verbose, _file, _output = cli_parser()

    try:
        if _A:
            print '\n \n A-Record for %s: \n %s \n \n' % (_domain, resolve.check_dns_a(_addr, _domain))

        if _AAAA:
            print '\n \n AAAA-Record for %s: \n %s \n \n' % (_domain, resolve.check_dns_aaaa(_addr,_domain))

        if _MX:
            print '\n \n MX-Record for %s: \n %s \n \n' % (_domain, resolve.check_dns_mx(_addr,_domain))

        if _SOA:
            print '\n \n SOA-Record for %s: \n %s \n \n' % (_domain, resolve.check_dns_soa(_addr,_domain))

        if _TXT:
            print '\n \n TXT-Record for %s: \n %s \n \n' % (_domain, resolve.check_dns_ns(_addr,_domain))

        if _NS:
            print '\n \n NS-Record for %s: \n %s \n \n' % (_domain, resolve.check_dns_ns(_addr,_domain))

        if _CNAME:
            try:
                print '\n \n CNAME-Record for %s: \n %s \n \n' % (_domain, resolve.check_dns_cname(_addr,_domain))
            except Exception as f:
                print (f)

        if _DHCID:
            if resolve.check_dns_dhcid(_addr,_domain) != '':
                print '\n \n DHCID-Record for %s: \n %s \n \n' % (_domain, resolve.check_dns_dhcid(_addr,_domain))

    except Exception as e:
        print (e)
    

def main():

    

    return dns_propogation()





if __name__ == "__main__":
  try:  
    main()
  except KeyboardInterrupt:
    print ' Interrupted'
  try:
    sys.exit(0)
  except SystemExit:
    os._exit(0)