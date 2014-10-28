from Bio import SeqIO
import numpy as np

def Length_db(Inputdb):
    """COMMENTS
    Inputdb must be a path to a fasta db"""
    ListLengthProt=[len(seq.seq) for seq in SeqIO.parse(Inputdb, 'fasta')]
    Mini=min(ListLengthProt)
    Maxi=max(ListLengthProt)
    Mean=np.mean(ListLengthProt)
    print Mini
    print Maxi
    print Mean
    return ListLengthProt
    




##
testdb=open('D:\\CLUSTER_RXLR20140309\\All_RxLR_20131212_aa_simpleName_EER_trunc20131212.fasta')
TestdbList=Length_db(testdb)
testdb2=open('D:\\Clustering20131212\\Combined_TrimmedPi_and_Pc_20131212.fasta')
Length_db(testdb2)
testdb3=open('D:\\Clustering20131212\\Try_Extended_RXLR_BLAST\\RXLRExtended_20140408.fasta')
Length_db(testdb3)

IdShorts=[seq for seq in SeqIO.parse(testdb, 'fasta') if len(seq.seq)<20]
