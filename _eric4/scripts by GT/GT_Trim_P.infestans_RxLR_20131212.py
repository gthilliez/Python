from Bio import SeqIO
import re
import time #to define date
date='%s%s%s'%(time.localtime()[0], time.localtime()[1], time.localtime()[2])#use in naming of files

##---for test only, inactivate if unused---#
import os
os.chdir('D:\Clustering20131212')
##---#

PiAllProt=open('phytophthora_infestans_t30-4_1_proteins.fasta')#File containing all predicted protein from P. infestans (fasta format)
PiOutFile=open('TrimmedPiProt%s.fasta'%date, 'w') #open the output file in writing mode
PITGdict = {} #create a dictionary, key will be name of protein and entry will be sequence

for s in SeqIO.parse(PiAllProt, 'fasta'): # file dictionnary with name and sequences info from the P. infestans predicted protein set
        PITGdict[s.id.replace('T0', '_1')] = s


Length1=len(PITGdict)#Get the number of P. infestans protein seq before replacing full length RXLR by truncated ones

PiTruncRxLRFile=open('P.infestans_RxLR_20131212_aa_simpleName_EER_trunc20131212.fasta') #path to the truncated RxLR dataset

for indexRXLR, seq in enumerate(SeqIO.parse(PiTruncRxLRFile, 'fasta')):
    PITGdict[seq.id]=seq


Length2=len(PITGdict)
if Length1!=Length2:
    print 'error'



print '%s full length predicted RXLR sequences have been replaced by truncated sequences'%(indexRXLR+1)
toWrite=[]
for key in PITGdict.iterkeys():
    toWrite.append(PITGdict.get(key))


SeqIO.write(toWrite, PiOutFile, 'fasta')


    
PiOutFile.close()
    
