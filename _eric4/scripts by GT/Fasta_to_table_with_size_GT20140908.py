from sys import stdin, argv

def CreateSizeTable(fasta):
    """Take a fasta file and create a table with
    col 1 as name
    col 2 as size
    col 3 as sequence
    Should work for both protein and nucleotidique sequence
    Requires Python 2.7 or more recent (not sure about python 3) and Biopython"""
    from Bio import SeqIO
    fh=open(fasta, 'r')
    fileout=open('%s_table.csv'%fasta, 'w')
    for s in SeqIO.parse(fh, 'fasta'):
        print>>fileout, '%s,%s,%s'%(s.id, len(s.seq), s.seq)


CreateSizeTable(argv[1])
