from Bio.Blast import NCBIXML
import xml.etree.cElementTree as cET
import os
#import csv
oname= raw_input('Enter output filename: ')
ofout=open(oname,'w')
tempfout=open('NCBIBLASTPARSER.csv', 'w')
if os.path.exists(oname):
    print'outfile ok'
else:
    print('Output file is not writable, check that the path of the file is correct and that Python have the right to modify the destination folder')
print>>tempfout,  'query,sbjct,e_value,bitscore,align_length,query_length,'
iname= raw_input('Enter path to blastoutput.xml: ')
Hrank=open('Hrank.csv', 'w')
print>> Hrank,  'Hit_rank'+','
for event, element in cET.iterparse(open(iname)):
    if 'Hit_num' in element.tag:
        print>>Hrank,  element.text +','
Hrank.close()
for record in NCBIXML.parse(open(iname)):
        for align in record.alignments:
            for hsp in align.hsps :
			print>>tempfout,  "%s,%s,%e,%f,%d,%d" \
			% (record.query, align.title[14:30], hsp.expect, hsp.bits, align.length, record.query_length,)
tempfout.close()
##f1=open('Hrank.csv', 'r')
##f2=open('NCBIBLASTPARSER.csv'.'r')
##Ziper=zip(f1, f2)
##print>>ofout,  Ziper
##ofout.close()
#fg = csv.DictReader(open('Hrank.csv', 'rb'), delimiter = ',')
#bg = csv.DictReader(open('NCBIBLASTPARSER.csv', 'rb'), delimiter = ',')
#fieldnames = fg.fieldnames+bg.fieldnames
#merged_file = csv.DictWriter(open(merged_path, 'ab'), delimiter = ',', fieldnames=fieldnames)
#merged_file.writeheader()
#for row in fg:
#    merged_file.writerow(row)
#for row in bg:
#    merged_file.writerow(row)
#merged_file.close()
##f1=csv.reader('Hrank.csv',delimiter=',')          
##f2=csv.reader('NCBIBLASTPARSER.csv',delimiter=',')
##mydict = {}
##for row in f1:
#    #mydict[row[0]] = row[0]
##for row in f2:
#    #mydict[row[1:]]=row[0:]
##ofout.write(mydict)
##ofout.close()
