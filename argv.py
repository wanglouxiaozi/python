#!/usr/bin/env python2

import sys, getopt


def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
		print opts
		print args
	except getopt.GetoptError:
		print 'argv.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'argv.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	print "input: ", inputfile
	print "output: ", outputfile
	

if __name__ == "__main__":
	main(sys.argv[1:])
	print sys.argv[0]
	print sys.argv[1]
	print sys.argv[2]
