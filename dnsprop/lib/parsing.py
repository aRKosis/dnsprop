#!/bin/usr/env python
class parser_exception(Exception):
    # base exc handler
    pass

class parser_operations(object):

    A_RECORD = "IN A "
    MX_RECORD = "IN MX "
    TXT_RECORD = "IN TXT "
    SPF_RECORD = "IN SPF "
    CNAME_RECORD = "IN CNAME "
    AAAA_RECORD = "IN AAAA "
    TXT = []
    MX = []
    A = []
    SPF = []
    AAAA = []
    CNAME = []

    def __init__(self, verbose=False):
        """
        Populates init.
        """
        self.verbose = verbose
        self.arecords = []
        self.mxrecords = []
        self.txtrecords = []
        self.cnamerecords = []
        self.aaaarecords = []
        self.spfrecords =[]

    def populate_zone(self, zone):
        """
        Opens file and returns a list of lines:
        zone = list of strings of a zone
        """
        for rec in zone:
            if self.A_RECORD in rec[0]:
                self.A.append(rec)
            elif self.MX_RECORD in rec[0]:
                self.MX.append(rec)
            elif self.TXT_RECORD in rec[0]:
                self.TXT.append(rec)
            elif self.CNAME_RECORD in rec[0]:
                self.CNAME.append(rec)
            elif self.AAAA_RECORD in rec[0]:
                self.AAAA.append(rec)
            elif self.SPF_RECORD in rec[0]:
                self.SPF.append(rec)

    def parse_zone(self):
        """
        Parse the entire zone populated.
        returns -> dict of record lists with dict. 
        """
        self.parse_zone_a()
        self.parse_zone_mx()
        self.parse_zone_txt()
        self.parse_zone_spf()
        obj = {'a_records' : self.arecords, 'mx_records' : self.mxrecords, 'txt_records' : self.txtrecords, "spf_records" : self.spfrecords}
        return obj

    def parse_zone_a(self):
        """
        Parse the A record format and 
        return a list of dict of values.
        record = list of A records to parse

        format:
         @ 10800 IN A 123.123.123.12
        """
        for a in self.A:
            parts = a[0].split()
            self.arecords.append({'name':parts[0],'ttl':parts[1],'record_class':parts[2],'record_type':parts[3],'record_data':parts[4]})

    def parse_zone_mx(self):
        """
        Parse the MX record format and 
        return a list of dict values.
        records = list of MX records to parse

        format:
        @ 10800 IN MX 10 spool.mail.gandi.net. 
        """
        for a in self.MX:
            parts = a[0].split()
            self.mxrecords.append({'name':parts[0],'ttl':parts[1],'record_class':parts[2],'record_type':parts[3],'record_pref':parts[4],'record_data':parts[5]})

    def parse_zone_txt(self):
        """
        Parse the TXT record format and
        return a list of dict values.
        records = list of TXT records to parse

        format:
        www 10800 IN TXT "insert information here"
        """
        for a in self.TXT:
            stage_one = a[0].split('"')
            parts = stage_one[0].split()
            self.txtrecords.append({'name':parts[0],'ttl':parts[1],'record_class':parts[2],'record_type':parts[3],'record_data':stage_one[1]})

    def parse_zone_spf(self):
        """
        Parse the SPF record format and
        return a list of dict values.
        records = list of TXT records to parse

        format:
        www 10800 IN SPF "v=spf1 +mx +a -all"
        """
        for a in self.SPF:
            stage_one = a[0].split('"')
            parts = stage_one[0].split()
            self.spfrecords.append({'name':parts[0],'ttl':parts[1],'record_class':parts[2],'record_type':parts[3],'record_data':stage_one[1]})



