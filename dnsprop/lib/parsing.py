#!/bin/usr/env python
class parser_exception(Exception):
    # base exc handler
    pass

class parser_operations(object):

    A_RECORD = "IN A "
    MX_RECORD = "IN MX "
    TXT_RECORD = "IN TXT "
    CNAME_RECORD = "IN CNAME "
    AAAA_RECORD = "IN AAAA "

    def __init__(self, verbose=False):

        try:
            self.verbose = verbose
        except Exception as e:
            print e

    def parse_zone(self, zone):
        """
        Opens file and returns a list of lines:
        zone = list of strings of a zone
        """
        a_list = []
        mx_list = []
        txt_list = []
        cname_list = []
        aaaa_list = []
        for rec in zone:
            if self.A_RECORD in rec:
                a_list.append(rec)
            elif self.MX_RECORD in rec:
                txt_list.append(rec)
            elif self.TXT_RECORD in rec:
                txt_list.append(rec)
            elif self.CNAME_RECORD in rec:
                cname_list.append(rec)
            elif self.AAAA_RECORD in rec:
                aaaa_list.append(rec)

    def parse_zone_a(self, records):
        """
        Parse the A record format and 
        return a list of dict of values.
        record = list of A records to parse

        format:
        NAME - TTL - IN - A - IP
        """
        a_list = []
        for a in records:
            parts = a.split()
            a_list.append({'name':parts[0],'ttl':parts[1],'record_class':parts[2],'record_type':parts[3],'record_data':parts[4]})
        return a_list



