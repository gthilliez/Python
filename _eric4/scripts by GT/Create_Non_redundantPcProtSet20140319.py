from Bio import SeqIO
import os

RXLRset=open('D:\Databases\RXLR_20131212\All_RxLR_20131212_aa.fasta')


TrimmedPcSet=open('D:\Clustering20131212\TrimmedPcapsiciSeq20131212.fasta')

SequenceDic={seq.name:seq
for seq in SeqIO.parse(TrimmedPcSet, 'fasta')}

len(SequenceDic)

for SeqRxLR in SeqIO.parse(RXLRset, 'fasta'):
    if 'PcRxLR' in SeqRxLR.name:
        SequenceDic[SeqRxLR.name]=SeqRxLR


len(SequenceDic)

ToWrite=[SequenceDic.get(k)
for k in SequenceDic]

fileout=open('D:\Databases\RXLR_20131212\NonRedundant_capsici_predicited_protein_with_CRN_and_RXLR_20140319.fasta', 'w')
SeqIO.write(ToWrite, fileout, 'fasta')

fileout.close()
