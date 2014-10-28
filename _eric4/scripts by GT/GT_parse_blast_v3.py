from Bio.Blast import NCBIXML
import os
oname= raw_input('Enter output filename: ')
ofout=open(oname,'w')
if os.path.exists(oname):
    print'outfile ok'
else:
    print('Output file is not writable, check that the path of the file is correct and that Python have the right to modify the destination folder')
iname= raw_input('Enter path to blastoutput.xml: ')
E_VALUE_THRESH = 1
for record in NCBIXML.parse(open(iname)):
	print>>ofout,  "QUERY: %s" % record.query
	for align in record.alignments:
		print>>ofout,  " MATCH: %s..." % align.title
		for hsp in align.hsps :
			print>>ofout,  " HSP, e=%e, bitscore=%f, from position %i to %i" \
			% (hsp.expect, hsp.bits, hsp.query_start, hsp.query_end)
			print>>ofout,  "  Query: %s" % hsp.query
			print>>ofout,  "  Match: %s" % hsp.match
			print>>ofout,  "  Sbjct: %s" % hsp.sbjct
            print>>ofout, ''

ofout.close
