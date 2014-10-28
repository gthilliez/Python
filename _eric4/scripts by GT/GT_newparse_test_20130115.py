
# script by Gaetan Thilliez 2013


from Bio.Blast import NCBIXML
import os
import re

oname= raw_input('Enter output filename: ')
ofout=open(oname,'w')
if os.path.exists(oname):
    print'outfile ok'
else:
    print('Output file is not writable, check that the path of the file is correct and that Python have the right to modify the destination folder')
print>>ofout,  'query,sbjct,e_value,bitscore,hit_length,query_length,align_length,hit_rank,percentage_id,percentage_coverage_query,percentage_coverage_hit'
iname= raw_input('Enter path to blastoutput.xml: ')
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
                Pcname=re.search('PcRxLR..._1',align.title) #look only for the PcRxLRnumb_1 name and not the others, simplify the name in the output file
                print>>ofout, "%s,%s,%e,%f,%f,%f,%f,%f,%f,%f,%f" \
                % (record.query,Pcname.group(),hsp.expect,hsp.bits,align.length,record.query_length,hsp.align_length,count,Percentage_id,Percentage_coverage_query, Percentage_coverage_hit)
ofout.close()
