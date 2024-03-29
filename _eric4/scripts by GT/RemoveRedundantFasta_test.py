from Bio import SeqIO
from sys import stdin, argv

def RemoveRedundantFasta(fasta):
    """This script read a fasta file and look for redundancie in the file. 
            it uses SeqIO from Biopython; sequence redudancie is defined by the sequence object generated by SeqIO
            therefore, a sequence should be entierly duplicated to be considered as redundant. If two sequences just share the same id
            or the same sequence they would not be removed.
        Input is a fasta file. Output created by the script will be a fasta file in the same directory as the input file
        name of output = name of input + nr.fasta
        eg if input is FastaFile01.fasta; output will be FastaFile01.fasta_nr.fasta"""
    fh=open(fasta)
    ToWrite={}
    for index, seq in enumerate(SeqIO.parse(fh, 'fasta')):
        print index
        ToWrite[seq.id]=''

    if len(ToWrite)<index+1: #because index start from 0 and therefore the length of the input file is index+1 to start from 1
        print '%s seq in %s; %s sequences left after removing redundancy'%(index+1, fasta, len(ToWrite))
        fout=open('%s_nr.fasta'%(fasta),'w')
        fh.seek(0)
        for seq in SeqIO.parse(fh, 'fasta'):
            if seq.id in ToWrite:
                SeqIO.write(seq, fout, 'fasta')
    elif len(ToWrite)==index+1:
        print 'There is no redundant sequences in the fasta file provided : %s therefore no output file was created'%(fasta)
    else:
        print 'error, check the format of the input file, it should be a fasta file'



RemoveRedundantFasta(argv[1])
