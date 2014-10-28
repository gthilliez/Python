from sys import stdin, argv
#create a tabular file with the name of the sequence as a first column. the size as a second column

def GetSeqSize(Input, Output):
    """COMMENTS"""
    from Bio import SeqIO
    fh=open(Input)
    Dic={Seq.id:len(Seq.seq) for Seq in SeqIO.parse(Input, 'fasta')}
    Outfile=open(Output, 'w')
    for key in Dic.iterkeys():
        print>>Outfile,  '%s\t%s'%(key, Dic.get(key))
    else:
        Outfile.close()



GetSeqSize(argv[1], argv[2])
