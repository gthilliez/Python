from Bio import SeqIO
import os

def CreateFastaFromGFF(GFF, Fasta1,fileout='Output_fasta',  Fasta2=False, Fasta3=False ):
    from Bio import SeqIO
    import csv
    fh=open(GFF)
    dialect=csv.Sniffer().sniff(fh.read(2048))
    reader=csv.reader(fh, dialect)
    fh.seek(0)
    SeqIds=[line[0] 
        for line in reader]
    ToWrite=[]
    for seq in SeqIO.parse(Fasta1, 'fasta'):
        if '_'.join(seq.name.split('|')[1:3]) in SeqIds:
            ToWrite.append(seq)
    if Fasta2!=False:
        for seq in SeqIO.parse(Fasta2, 'fasta'):
            if seq.name in SeqIds:
                ToWrite.append(seq)
    if Fasta3!=False:
        for seq in SeqIO.parse(Fasta3, 'fasta'):
            if seq.name in SeqIds:
                ToWrite.append(seq)
    Out=open(fileout, 'w')
    SeqIO.write(fileout, ToWrite, 'fasta')
    print '%s seq wrote in %s'%(len(ToWrite), fileout)





