#!/bin/usr/env python

import dns.query
import dns.resolver

class dns_exception(Exception):
    pass

class dnsresolver(object):

    #TODO
    #VALID_RECORDS = ['A', 'MX', 'PTR', 'TXT', 'AAAA', 'CNAME', 'DHCHID', 'DNSKEY', 'IPSEC', 'KEY', 'NS', 'SIG', 'SRV', 'URI']

    def __init__(self, verbose=False):
        try:
            self.verbose = verbose
        except Exception as e:
            print e

    def check_dns_a(self, ip, query):
        """
        Checks a A Record for givin DNS server IP,
        using provided DNS name server.

        ip - name server for query
        query - the domain name for search
        """
        ipaddr = []
        dnsip = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver() # create a new instance named 'myResolver'
        my_resolver.nameservers = ipaddr
        
        myAnswers = my_resolver.query(query, 'A')  # Lookup the 'A' record(s) for google.com
        for a in myAnswers:
            dnsip.append(a.address)
        return dnsip

    def check_dns_mx(self, ip, query):
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
       
        myAnswers = my_resolver.query(query, 'MX')  # Lookup the 'MX' record(s) for google.com
        for a in myAnswers:
            dnsip.append(a.exchange)
        return dnsip

    def check_dns_ns(self, ip, query):
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
       
        myAnswers = my_resolver.query(query, 'NS')  # Lookup the 'A' record(s) for google.com
        for a in myAnswers:
            dnsip.append(a)
        return dnsip

    def check_dns_txt(self, ip, query):
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
        
        myAnswers = my_resolver.query(query, 'TXT')  # Lookup the 'A' record(s) for google.com
        for a in myAnswers:
            dnsip.append(a.address)
        return dnsip

