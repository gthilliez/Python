from Bio.Blast import NCBIXML
import os
import re
iname= raw_input('Enter path to blastoutput.xml: ')
#C:\Users\gt41237\Neighbourhood join\PinfvsPcap_truncated_aa_20130107.xml
oname= raw_input('Enter output filename: ')
ofout=open(oname,'w')
print>>ofout, 'query,sbjct,e_value,bitscore,hit_length,query_length,align_length,hit_rank,percentage_id,percentage_coverage_query,percentage_coverage_hit,deltaBitScore'
for record in NCBIXML.parse(open(iname)):
    count=0 #start a counter that correspond to the Hit_rank, and reset for each query
    for align in record.alignments:
        count += 1 #count hit rank
        count2=0 #start a counter to exclude the mutiple hit by subject
        for hsp in align.hsps:
            count2+=1 #start the excluding counter
            if count2==1: #only the first hit of a query on a subject will be conserved
                queryname='%s' %(record.query)
                Percentage_id=(hsp.identities*100/record.query_length)
                Percentage_coverage_query=(hsp.align_length*100/record.query_length)
                Percentage_coverage_hit=(hsp.align_length*100/align.length)
                Pcname=re.search('PcRxLR..._1',align.title) #look only for the PcRxLRnumb_1 name and not the others, simplify the name in the output file
                if queryname==queryname_previous:
                    deltaBitScore=(previous_bitscore-hsp.bits)
                    print 'the delta bit score is %f, hit rank %s - hit rank %s' %(deltaBitScore,previous_count,count)
                    print>>ofout, "%s,%s,%e,%f,%f,%f,%f,%f,%f,%f,%f,%f" \
                % (record.query,Pcname.group(),hsp.expect,hsp.bits,align.length,record.query_length,hsp.align_length,count,Percentage_id,Percentage_coverage_query,Percentage_coverage_hit,deltaBitScore)
                    queryname_previous=record.query
                    previous_bitscore=hsp.bits
                    previous_count=count
                else:
                    deltaBitScore_none='none'
                    print 'there is no previous hit for %s, %s, hit rank %f' %(record.query,Pcname.group(),count)
                    print>>ofout, "%s,%s,%e,%f,%f,%f,%f,%f,%f,%f,%f,%s" \
                % (record.query,Pcname.group(),hsp.expect,hsp.bits,align.length,record.query_length,hsp.align_length,count,Percentage_id,Percentage_coverage_query,Percentage_coverage_hit,deltaBitScore_none)
                    queryname_previous=record.query
                    previous_bitscore=hsp.bits
                    previous_count=count
            
