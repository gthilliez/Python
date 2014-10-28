#Create a BLAST output containing RXLRs and protein hitting RXLRs
#The aim is to get a smaller dataset focused on RXLRs and all protein potentially related to RXLRs


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
