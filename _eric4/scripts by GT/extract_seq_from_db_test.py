target='NbS00024222g0008.1'
from Bio import SeqIO
import os
os.chdir('D:\Databases\\benth')
fh=open('Niben.genome.v0.4.4.proteins.fasta')

Towrite=[]
for s in SeqIO.parse(fh, 'fasta'):
    if target in s.id:
        Towrite.append(s)



output=open('NbS00024222g0008.1_prot.fasta', 'w')
SeqIO.write(Towrite, output, 'fasta')
output.close()
