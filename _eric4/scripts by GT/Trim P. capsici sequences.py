#imports
from Bio.Blast import NCBIXML
import os
import re
from Bio.SeqUtils import quick_FASTA_reader
##dictionnaries
Phyca11PcRxLRdict={}
#PcRxLRseqdict={}
final_dict={}
anotherdict={}
##regular expression
regex=('jgi.{0,200}')
##output file
oname= raw_input('Enter output filename: ')
fileout=open(oname, 'w')
##the following code lines are here to read a blast out put, and select only the 100% match between predicted effector and predicted proteins
iname= raw_input('Enter path to blastoutput.xml: ')
for record in NCBIXML.parse(open(iname)):
    for align in record.alignments:
        for hsp in align.hsps:
            if hsp.identities == record.query_length:
                #Phyca11key="%s|%s"%(record.query, align.title)
                #Phyca11PcRxLRdict[Phyca11key]='none'
                norm_key_b=re.search(regex, align.title)
                n_key_b=norm_key_b.group()
                alt_Phyca11='%s'%(n_key_b)
                Phyca11PcRxLRdict[alt_Phyca11]='none'
                print "%s,%s,%e,%f,%f,%f,%f" \
                % (record.query,align.title,hsp.expect,hsp.bits,align.length,record.query_length,hsp.align_length)
                
##the following lines create a dictionnary of the P. capsici effector set, key is the name and value is the sequence
#iname2= raw_input('Enter path to P. capsici predicted RxLR set: ')
#entries = quick_FASTA_reader(iname2)
#for name, seq in entries:
#    PcRxLR_name=re.search('PcRxLR...', name)
#    PcRxLR_name_2=PcRxLR_name.group()
#    PcRxLRseqdict[PcRxLR_name_2]=seq
##following line give the sequence to the 100% match effector/predicted protein
#for key1 in Phyca11PcRxLRdict :
#    Pcname=re.search('PcRxLR...', key1)
#    for key2 in PcRxLRseqdict:
#        if Pcname.group()==key2:
#            value=PcRxLRseqdict.get(key2)
#            Phyca11PcRxLRdict[key1]=value
            
##create a dictionnary containing the predicted prot name as a key and their seq as a value
iname3=raw_input('Enter path to the P. capsici predicted protein file: ')
entries_2 = quick_FASTA_reader(iname3)
for name, seq in entries_2:
    final_dict[name]=seq
    anotherdict[name]=seq
##compare the name of the predicted protein and the name from the 100% match with effector. if a 100% match is in the predicted protein dictionnary, then it's removed
##as I cannot remove the value from final_dict, because it make the program crash, because the size of the dictionnary change between iteration and it make Python unhappy
##I have created a second dictionnary aka anotherdict that contain the same info as final_dict but i can remove value from anotherdict without making the program crash

for key_a in final_dict:
    norm_key_a=re.search(regex, key_a)
    n_key_a=norm_key_a.group()
    for key_b in Phyca11PcRxLRdict:
        norm_key_b=re.search(regex, key_b)
        n_key_b=norm_key_b.group()
        if n_key_a==n_key_b:
            print 'There is a match'
            anotherdict.pop(key_a)
##Now I have my set of predicted protein, without the RxLRs, so I can just append the truncated RxLRs to the dictionnary

iname4=raw_input('Enter path to the P. capsici truncated RxLR EER set: ')
entries_3 = quick_FASTA_reader(iname4)
for name, seq in entries_3:
    anotherdict[name]=seq
    
for key in anotherdict:
	print>>fileout, ">%s" %(key)
	print>>fileout, (anotherdict.get(key))
    
