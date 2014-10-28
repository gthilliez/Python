#The aim of the script is to parse a Blast output in XML format
#the information extracted from the blast output are listed on line 18
#the output format is CSV, each information is a column, each hit is a line
# script by Gaetan Thilliez 2013

#Import
from Bio.Blast import NCBIXML
import os
import re

oname= raw_input('Enter output filename: ')
ofout=open(oname,'w')
if os.path.exists(oname):
    print'outfile ok'
else:
    print('Output file is not writable, check that the path of the file is correct and that Python have the right to modify the destination folder')
#line 11 and 12 ask for the output file directory and create the file, line 12 to 15 check if the outfile is created
print>>ofout,  'query,sbjct,e_value,bitscore,hit_length,query_length,align_length,hit_rank,percentage_id,percentage_coverage_query,percentage_coverage_hit'
#line 18 give a header to the columns of the CSV
iname= raw_input('Enter path to blastoutput.xml: ')
#line 20 ask for the input, the file must be a blast out put in a XML format
for record in NCBIXML.parse(open(iname)):
    count=0 #start a counter that correspond to the Hit_rank, and reset for each query
    for align in record.alignments:
        count += 1 #count hit rank
        count2=0 #start a counter to exclude the mutiple hit by subject
        for hsp in align.hsps:
            count2+=1 #start the excluding counter
            if count2==1: #only the first hit of a query on a subject will be conserved
                Percentage_id=(hsp.identities*100/record.query_length)
                Percentage_coverage_query=(hsp.align_length*100/record.query_length)
                Percentage_coverage_hit=(hsp.align_length*100/align.length)
                Pcname=re.search('PcRxLR..._1',record.query) #look only for the PcRxLRnumb_1 name and not the others, simplify the name in the output file
                Piname=re.search('PITG_....._1', align.title)
                print>>ofout, "%s,%s,%e,%f,%f,%f,%f,%f,%f,%f,%f" \
                % (Pcname.group(),Piname.group(),hsp.expect,hsp.bits,align.length,record.query_length,hsp.align_length,count,Percentage_id,Percentage_coverage_query,Percentage_coverage_hit)
ofout.close()
#line 22, open the blastoutput.xml, record design every query showing at least one hit
#line 24 design every hit
#line 27 looks in the hsp
#line 30 31 32, calculate respectively the %id and coverage query and coverage of the hit
#line34 and 35 print the information listed on line 18 in the output file
#line 36 close the output file
