#!/bin/usr/env python
# handles all file opperations for dnsprop
class file_exception(Exception):
    # base exc handler
    pass

class file_operations(object):

    def __init__(self, verbose=False):
        try:
            self.verbose = verbose
        except Exception as e:
            print e

    def open_file_lines(self, filename):
        """
        Opens file and returns a list of lines:
        filename = pass str() name of file
        """
        ret = []
        try:
            with open(filename) as inputfile:
                for line in inputfile:
                    ret.append(line.strip().split('\n'))
            return ret
        except Exception as e:
            raise file_exception("Error opening file for reading list: %s" % (str(e)))

    def open_file_blob(self, filename):
        """
        Opens file and returns a file blob of data:
        filename = pass str() name of file
        """
        try:
            with open(filename) as inputfile:
                file_data = inputfile.read()
            return file_data
        except Exception as e:
            raise file_exception("Error opening file for reading: %s" % (str(e)))
