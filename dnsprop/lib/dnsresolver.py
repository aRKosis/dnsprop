#!/bin/usr/env python

import dns.query
import dns.resolver

class dnsresolver(object):

    VALID_RECORDS = ['A', 'MX', 'PTR', 'TXT', 'AAAA', 'CNAME', 'DHCHID', 'DNSKEY', 'IPSEC', 'KEY', 'NS', 'SIG', 'SRV', 'URI']

    def __init__(self, verbose=False):
        try:
            self.verbose = verbose
        except Exception as e:
            print e

    def check_dns_a(self, ip, query, record_type):
        """
        Checks a A Record for givin DNS server IP,
        using provided DNS name server.

        ip - name server for query
        query - the domain name for search
        """
        ipaddr = []
        dnsip = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver()  # create a new instance named 'myResolver'
        my_resolver.nameservers = ipaddr

        myAnswers = my_resolver.query(query, record_type)  # Lookup the 'A' record(s) for google.com
        for a in myAnswers:
            dnsip.append(a.address)
        return dnsip


