from sys import stdin, argv
#modify the script to add the motif and the span and look if there is several motif in one sequence
def KVXF_finder2 (fasta):
    """COMMENTS"""
    from Bio import SeqIO
    import re
    KVXF=re.compile('[HKR][ACHKMNQRSTV]{0,1}V[CHKNQRST][FW]')
    ToWrite=[seq for seq in SeqIO.parse(fasta, 'fasta') if re.search(KVXF,  str(seq.seq.upper()))]
    if len(ToWrite)>0:
        output=open('%s_KVFX_extended.fasta'%(fasta), 'w')
        SeqIO.write(ToWrite, output, 'fasta')
        output.close()
    else:
        print 'no KVXF motif found in the provided fasta file : %s'%fasta



KVXF_finder2(argv[1])

