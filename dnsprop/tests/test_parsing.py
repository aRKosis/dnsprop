from lib import files
from lib import parsing 

def test_parsing_zone():
	f = files.file_operations()
	f_list = f.open_file_lines('zone_test.txt')
	p = parsing.parser_operations()
	p.populate_zone(f_list)
	print p.TXT
	print p.A
	print p.SPF
	print p.AAAA
	print p.CNAME
	p.parse_zone_a()
	p.parse_zone_txt()
	print
	obj = p.parse_zone()
	for item in obj:
		print item + item[0]

test_parsing_zone()