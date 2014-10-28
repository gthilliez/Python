from sys import stdin, argv

def KVXF_finder (fasta):
    """COMMENTS"""
    from Bio import SeqIO
    import re
    KVXF=re.compile('KV.F')
    ToWrite=[seq for seq in SeqIO.parse(fasta, 'fasta') if re.search(KVXF,  str(seq.seq))]
    if len(ToWrite)>0:
        output=open('KVFX_%s'%(fasta), 'w')
        SeqIO.write(ToWrite, output, 'fasta')
        output.close()
    else:
        print 'no KVXF motif found in the provided fasta file : %s'%fasta



KVXF_finder(argv[1])

