import os
from Bio import SeqIO
from sys import stdin,argv

def CombineFasta (Folder, output):
    """COMMENTS
    Script by Gaetan Thilliez
    Requires Python 2.7 or newer and Biopython
    Folder must be folder containing only fasta file to combine
    output is the name of a file that will be created by the script and will contain
        all the sequences from the files present in 'Folder' """

    os.chdir(Folder)
    path=os.getcwd()
    Out=open(output, 'w')
    for file in os.listdir(path):
        if file not in Out.name:
            fh=open(os.path.join(path, file))
            for seq in SeqIO.parse(fh, 'fasta'):
                SeqIO.write(seq, Out, 'fasta')
    else:
        Out.close()


CombineFasta(argv[1], argv[2])
