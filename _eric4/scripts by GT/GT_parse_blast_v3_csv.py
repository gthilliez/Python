from Bio.Blast import NCBIXML
import os
oname= raw_input('Enter output filename: ')
ofout=open(oname,'w')
if os.path.exists(oname):
    print'outfile ok'
else:
    print('Output file is not writable, check that the path of the file is correct and that Python have the right to modify the destination folder')
print>>ofout,  'query,sbjct,e_value,bitscore,align_length,query_length'
iname= raw_input('Enter path to blastoutput.xml: ')
E_VALUE_THRESH = 1
for record in NCBIXML.parse(open(iname)):
	for align in record.alignments:
		for hsp in align.hsps :
			print>>ofout,  "%s,%s,%e,%f,%d,%d" \
			% (record.query, align.title[14:30], hsp.expect, hsp.bits, align.length, record.query_length, )
ofout.close()
