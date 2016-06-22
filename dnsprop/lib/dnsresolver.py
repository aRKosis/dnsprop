#!/bin/usr/env python

import dns.query
import dns.resolver

class dnsresolver(object):

    def __init__(self, verbose=False):
        try:
            self.verbose = verbose
        except Exception as e:
            print e

    def check_dns(self, ip, quer):
        ipaddr = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver()  # create a new instance named 'myResolver'
        my_resolver.nameservers = ipaddr

        myAnswers = my_resolver.query(quer, 'A')  # Lookup the 'A' record(s) for google.com
        for a in myAnswers:
            print a.address
