##The aim of this script is to extract seq from a fasta file and create a new fasta file

from sys import stdin,argv

def ExtractFastaSeq (List, Fasta, output):
    """List must be a path to a list of name ,matching the names in the Fasta
    Fasta is a path to a Fasta file, sequences from fasta will be extracted if they are in the List
    output is a path to an output file that will be created"""
    from Bio import SeqIO
    FastaFh=open(Fasta)
    ListFh=open(List)
    SeqList=[element.strip().lower() for element in ListFh]
    Towrite=[seq 
    for seq in SeqIO.parse(FastaFh,'fasta')
    if seq.name.lower() in SeqList]
    print '%s sequences found'%(len(Towrite))
    print '%s sequences missing'%(len(SeqList)-len(Towrite))
    outputfile=open(output, 'w')
    SeqIO.write(Towrite, outputfile, 'fasta')


ExtractFastaSeq(argv[1], argv[2], argv[3])
