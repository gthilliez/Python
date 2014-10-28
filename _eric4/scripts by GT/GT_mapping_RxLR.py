#This script aim to map the predicted RxLRs effector from P. capsici on the genome to identify the corresponding transcript.
#The default of this script is that it might get rid of transcript that are not predicted RxLR but for which
#the position is overlaping with predicted RxLRs on the genome 
#2013 Gaëtan Thilliez
import re
from Bio.SeqUtils import quick_FASTA_reader
#The table containing the PcRxLR / Phycascaffold name equivalence will allow us to map the RxLR on the genome (Phycascaffold name contain the position)
#the problem is that this table have been created based on blast. So it is impossible to make a difference between two duplication of the same gene located at different position on the genome
#with this version of the table eg PcRxLR008 and PcRxLR009
iname= raw_input('Enter path to table containing PcRxLR and PHYCAscaffold names: ')
file_handle=open(iname,'rb')
oname= raw_input('Enter output filename: ')
fileout=open(oname, 'w')

oname2= raw_input('Enter output filename: ')
fileout2=open(oname2, 'w')

Phycascaffold_regex_1= re.compile('PHYCAscaffold_[0-9]{1,3}')
RxLRdict={}

for row in file_handle:
    try:
        PHYCAscaf_search=re.search(Phycascaffold_regex_1,  row)
        PHYCAscaf_numb='%s'%(PHYCAscaf_search.group())
        print PHYCAscaf_numb
        Pcsearch=re.search('PcRxLR...', row)
        Pcname='%s'%(Pcsearch.group())
        splitregex=re.search('[0-9]{3,8}_[0-9]{3,8}_[0-9]',  row)
        splitted='%s'%(splitregex.group())
        n1 = splitted.split('_')
        #print '%s'%(n1)
        frame='%s'%(n1[2])
        #print frame
        if int(frame)<4:
            print'no probleme with the if statement'
            start=int(n1[0])
            stop=int(n1[1])
            RxLRdict[Pcname]=start,  stop, n1[2], PHYCAscaf_numb
            #print '%s'%( start)
        else:
            print'no probleme with the else statement'
            start=int(n1[1])
            stop=int(n1[0])
            RxLRdict[Pcname]=start,  stop, n1[2], PHYCAscaf_numb
            #print '%s'%(start)
        #print Pcname
    except:
        continue
#The part of the script described above store the position of the predicted RxLR in a Dictionary called RxLRDict

##start=n1[0]
##stop=n1[1]
##frame=n1[2]
##if start <stop, strand = +
##if stop>strat strand = -
##i assume that if frame is 1-3, stand is +
##if frame is 4-6 strand is -

##now i need to read the GFF file, isolate the start and stop codon and compare them to the one from the RxLR list
iname2= raw_input('Enter path to the GFF file from http://genome.jgi-psf.org: ')
file_handle2=open(iname2,'rb')
GFFdict={}
for row in file_handle2:
    data=row.split()
    if '+' in data:
        if 'CDS' in data:
            Phycaname='%s_%s_%s'%(data[0], int(data[3]), int(data[4]))
            start=int(data[3])
            stop=int(data[4])
            ID=re.search('[0-9]{1,8}',data[11])
            GFFdict[Phycaname]=start, stop, data[0], ID.group()
            print '+ %s'%(Phycaname)
        else:
            continue
    else:
        if '-'in data:
            if 'CDS' in data:
                Phycaname='%s_%s_%s'%(data[0], int(data[3]), int(data[4]))
                stop=int(data[3])
                start=int(data[4])
                ID=re.search('[0-9]{1,8}',data[11])
                GFFdict[Phycaname]=start, stop, data[0], ID.group()
                print '- %s'%(Phycaname)
            else:
                continue
        else: 
            print 'script cannot work'
#This part store the location of the predicted protein from the V11 of the P.capsici genome
dictPotentialOverlap={}

for key1 in RxLRdict:
    for key2 in GFFdict:
        if RxLRdict[key1][3]==GFFdict[key2][2]:
            if (int(RxLRdict[key1][0])-3)<=GFFdict[key2][0]<=(int(RxLRdict[key1][1])+3):
                deltastart=RxLRdict[key1][0]-GFFdict[key2][0]
                deltastop=RxLRdict[key1][1]-GFFdict[key2][1]
                key3='%s_%s'%(key1, key2)
                dictPotentialOverlap[key3]=deltastart, deltastop, key2, RxLRdict[key1][3], int(RxLRdict[key1][0]), int(RxLRdict[key1][1]), int(GFFdict[key2][3])
            if (int(RxLRdict[key1][0])-3)>=GFFdict[key2][0]>=(int(RxLRdict[key1][1])+3):
                deltastart=RxLRdict[key1][0]-GFFdict[key2][0]
                deltastop=RxLRdict[key1][1]-GFFdict[key2][1]
                key3='%s_%s'%(key1, key2)
                dictPotentialOverlap[key3]=deltastart, deltastop, key2, RxLRdict[key1][3], int(RxLRdict[key1][0]), int(RxLRdict[key1][1]), int(GFFdict[key2][3])
            if (int(RxLRdict[key1][0])-3)>=GFFdict[key2][1]>=(int(RxLRdict[key1][1])+3):
                deltastart=RxLRdict[key1][0]-GFFdict[key2][0]
                deltastop=RxLRdict[key1][1]-GFFdict[key2][1]
                key3='%s_%s'%(key1, key2)
                dictPotentialOverlap[key3]=deltastart, deltastop, key2, RxLRdict[key1][3], int(RxLRdict[key1][0]), int(RxLRdict[key1][1]), int(GFFdict[key2][3])
            if (int(RxLRdict[key1][0])-3)<=GFFdict[key2][1]<=(int(RxLRdict[key1][1])+3):
                deltastart=RxLRdict[key1][0]-GFFdict[key2][0]
                deltastop=RxLRdict[key1][1]-GFFdict[key2][1]
                key3='%s_%s'%(key1, key2)
                dictPotentialOverlap[key3]=deltastart, deltastop, key2, RxLRdict[key1][3], int(RxLRdict[key1][0]), int(RxLRdict[key1][1]), int(GFFdict[key2][3])
        else:
            continue
#This section above compare the location of the predicted protein set and the ones from the predicted RxLR set. 
##need to check the value in the dictPotentialOverlap
dictPotentialOverlap['PcRxLR515']='none', 'none', 'none', 'none', 'none', 'none', 39353
dictPotentialOverlap['PcRxLR516']='none', 'none', 'none', 'none', 'none', 'none', 531755
#Those two lines aboves add manually the effector PcRxLR 515 and 516 because they were not in the table loaded at line 10
for key in dictPotentialOverlap:
	print>>fileout, ">%s" %(key)
	print>>fileout, (dictPotentialOverlap.get(key))
Phyca11_dict1={}
Phyca11_dict2={}
iname3=raw_input('Enter path to the P. capsici predicted protein file: ')
entries_2 = quick_FASTA_reader(iname3)
for name, seq in entries_2:
    data2=name.split('|')
    Identifier=int(data2[2])
    Phyca11_dict1[Identifier]=seq
    Phyca11_dict2[Identifier]=seq

Newdict={}
for keya in Phyca11_dict1:
    for keyb in dictPotentialOverlap:
        if int(keya)==dictPotentialOverlap[keyb][6]:
            try:
                Phyca11_PcRxLR="%s,%s"%(keya, keyb)
                Newdict[Phyca11_PcRxLR]=Phyca11_dict1.get(keya)
                Phyca11_dict2.pop(keya)
            except:
                print 'Phyca11|%s is not in the predicted protein set'%(keya)
#If there is overlap, even partial, then only the RxLR seq is kept. If the RxLR seq is not in the protein predicted set, it is added
newfileout=open('C:\Users\gt41237\Overlapping_protein_with_PcRxLR.csv', 'wb')
for key in Newdict:
    print>>newfileout,  "%s,%s"%(key, Newdict.get(key))
newfileout.close()

iname4=raw_input('Enter path to the P. capsici truncated RxLR EER set: ')
entries_3 = quick_FASTA_reader(iname4)
for name, seq in entries_3:
    Phyca11_dict2[name]=seq

for key in Phyca11_dict2:
    try:
        Idname=re.search('PcRxLR', key)
        print>>fileout2, ">%s" %(key)
        print>>fileout2, (Phyca11_dict2.get(key))
    except:
        print>>fileout2, ">Phyca11|%s" %(key)
        print>>fileout2, (Phyca11_dict2.get(key))
        continue
        
#Those section aboves are there to create an output file
