#!/bin/usr/env python

import dns.query
import dns.resolver

class dns_exception(Exception):
    pass

class dnsresolver(object):

    #TODO
    #VALID_RECORDS = ['A', 'MX', 'PTR', 'TXT', 'AAAA', 'CNAME', 'DHCID', 'DNSKEY', 'IPSEC', 'KEY', 'NS', 'SIG', 'SRV', 'URI']

    def __init__(self, verbose=False):
        try:
            self.verbose = verbose
        except Exception as e:
            print e

    def check_dns_a(self, ip, query):
        """
        Checks for the A Record of the
        domain, given the DNS server IP,

        ip - IP addr of name server
        query - the domain name for search
        """
        ipaddr = []
        dnsip = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver() # create a new instance named 'myResolver'
        my_resolver.nameservers = ipaddr
        
        myAnswers = my_resolver.query(query, 'A')  # Lookup the 'A' record(s)
        for a in myAnswers:
            dnsip.append(a.address)
        return dnsip

    def check_dns_mx(self, ip, query):
        """
        Checks for the MX Record of the
        domain, given the DNS server IP,

        ip - IP addr of name server
        query - the domain name for search
        """
        ipaddr = []
        dnsip = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver()
        my_resolver.nameservers = ipaddr
       
        myAnswers = my_resolver.query(query, 'MX')  # Lookup the 'MX' record(s)
        for a in myAnswers:
            dnsip.append(a.exchange)
        return dnsip

    def check_dns_ns(self, ip, query):
        """
        Checks for the NS Record of the
        domain, given the DNS server IP,

        ip - IP addr of name server
        query - the domain name for search
        """
        ipaddr = []
        dnsip = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver()
        my_resolver.nameservers = ipaddr
       
        myAnswers = my_resolver.query(query, 'NS')  # Lookup the 'NS' record(s)
        for a in myAnswers:
            dnsip.append(a)
        return dnsip

    def check_dns_txt(self, ip, query):
        """
        Checks for the TXT Record of the
        domain, given the DNS server IP,

        ip - IP addr of name server
        query - the domain name for search
        """
        ipaddr = []
        dnsip = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver()
        my_resolver.nameservers = ipaddr
        
        myAnswers = my_resolver.query(query, 'TXT')  # Lookup the 'TXT' record(s) 
        for a in myAnswers:
            dnsip.append(a)
        return dnsip

    def check_dns_aaaa(self, ip, query):
        """
        Checks for the AAAA Record of the
        domain, given the DNS server IP,

        ip - IP addr of name server
        query - the domain name for search
        """
        ipaddr = []
        dnsip = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver()
        my_resolver.nameservers = ipaddr
        
        myAnswers = my_resolver.query(query, 'AAAA')  # Lookup the 'AAAA' record(s) 
        for a in myAnswers:
            dnsip.append(a.address)
        return dnsip

    def check_dns_cname(self, ip, query):
        """
        Checks for the CNAME Record of the
        domain, given the DNS server IP,

        ip - IP addr of name server
        query - the domain name for search
        """
        ipaddr = []
        dnsip = []
        ipaddr.append(ip)
        my_resolver = dns.resolver.Resolver()
        my_resolver.nameservers = ipaddr
        
        myAnswers = my_resolver.query(query, 'CNAME')  # Lookup the 'CNAME' record(s)
        for a in myAnswers:
            dnsip.append(a.target)
        return dnsip

    # def check_dns_dhcid(self, ip, query):
    #     """
    #     Checks for the DHCID Record of the
    #     domain, given the DNS server IP,

    #     ip - IP addr of name server
    #     query - the domain name for search
    #     """
    #     ipaddr = []
    #     dnsip = []
    #     ipaddr.append(ip)
    #     my_resolver = dns.resolver.Resolver()
    #     my_resolver.nameservers = ipaddr
        
    #     myAnswers = my_resolver.query(query, 'DHCID')  # Lookup the 'DHCID' record(s)
    #     for a in myAnswers:
    #         dnsip.append(a)
    #     return dnsip