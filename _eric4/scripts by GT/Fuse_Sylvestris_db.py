from Bio import SeqIO
import textwrap

Fp='D:\Databases\Genomes_sequences\sylvestris\ASAF01.fsa.1'
FH=open(Fp, 'r')

SeqList=[(rec.id, rec.seq)
         for rec in SeqIO.parse(FH, 'fasta')]


Fp2='D:\Databases\Genomes_sequences\sylvestris\ASAF01.fsa.2'
FH2=open(Fp, 'r')

SeqList2=[(rec.id, rec.seq)
         for rec in SeqIO.parse(FH2, 'fasta')]


Fp3='D:\Databases\Genomes_sequences\sylvestris\ASAF01.fsa.3'
FH3=open(Fp, 'r')

SeqList3=[(rec.id, rec.seq)
         for rec in SeqIO.parse(FH3, 'fasta')]
         
TotalSeqList=[element for element in SeqList+SeqList2+SeqList3]
FileoutP='D:\Databases\Genomes_sequences\sylvestris\Sylvestris_fsa1-2-3fused.fasta'
FileoutH=open(FileoutP, 'w')

for element in TotalSeqList:
    print>>FileoutH,  '>%s'%element[0]
    print>>FileoutH,  '\n'.join(textwrap.wrap(str(element[1]), 80))


FileoutH.close()
