from Bio import SeqIO
from sys import stdin, argv

def GetSeqFromGenome (GenomeDb,  Scaffold, Start, Stop):
    """COMMENTS"""
    for seq in SeqIO.parse(GenomeDb, 'fasta'):
        if Scaffold in seq.id:
            print 'sequence found'
            print len(seq)
            SeqtoWrite=seq[int(Start):(int(Stop)+1)]
            Output=open('Output_%s.fasta'%Scaffold, 'w')
            SeqIO.write(SeqtoWrite, Output, 'fasta')
            print '%s Start:%s Stop:%s len:%s written in %s'%(Scaffold, Start, Stop, len(SeqtoWrite), Output.name)
            Output.close()
            break



GetSeqFromGenome(argv[1], argv[2], argv[3], argv[4])
