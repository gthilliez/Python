#Create a BLAST output containing RXLRs and protein hitting RXLRs
#The aim is to get a smaller dataset focused on RXLRs and all protein potentially related to RXLRs

import os

def fastaDataset(format='fasta', *args):
    """Comments
    format must be a string (see help(bio.SeqIO) for details
    *args must be valid path to a file corresponding to format
    to use : 
    Variable=fastaDataset('fasta',arg)"""
    from Bio import SeqIO
    FastaDic={}
    for arg in args:
        fh=open(arg)
        print "%s is open"%arg
        for seq in SeqIO.parse(arg, format):
            FastaDic[seq.name]=seq
    else:
        return FastaDic



os.chdir('D:\Databases\RXLR_20131212')
RXLRFile='All_RxLR_20131212_aa_simpleName_EER_trunc20131212.fasta'
RXLRDic=fastaDataset('fasta',RXLRFile)


import csv
BLASTFile='D:\Clustering20131212\BLAST\SelfBLAST_Combined_TrimmedPi_and_Pc_20131212.fasta.defaultEvalue.txt'
fh=open(BLASTFile)
BLAST={}
for unformatedLine in fh:
    line=unformatedLine.strip().split('\t')
    BLAST[line[0]]=line



ExtendedRXLR=[k 
                        for k in RXLRDic]
oldlen=len(ExtendedRXLR)
newlen=0
while oldlen !=newlen:
    oldlen=len(ExtendedRXLR)
    for k in ExtendedRXLR:
        if k in BLAST:
            Hit=BLAST.get(k)[1]
            if Hit not in ExtendedRXLR:
                ExtendedRXLR.append(Hit)
    else:
        newlen=len(ExtendedRXLR)


#length of extended list is quite small. Double check
ToWrite=[]
for k in ExtendedRXLR:
    if k in BLAST:
        ToWrite.append(BLAST.get(k))


BLASTOutput=open('BLASTOutput_RXLRExtended_20140408.csv', 'w')
for element in ToWrite:
    print>>BLASTOutput, "%s"%','.join(element)
else:
    BLASTOutput.close()

