import os
from Bio import SeqIO

def CutSignalPeptide(Fasta, SignalP, SignalPSelectionColumn=2, SignalPHeader=True, IncludeStart=True):
    """COMMENTS"""
    FastaFh=open(Fasta)
    SignalPFh=open(SignalP)
    FastaDic={Seq.id:Seq for Seq in SeqIO.parse(FastaFh, 'fasta')}
    if SignalPHeader==True:
        skipHeader=SignalPFh.readline()
    for unformatedline in SignalPFh:
        line=unformatedline.strip().split('\t')
        id=line[0]
        StartMatureProt=int(line[2])
        FastaDic[id]=FastaDic.get(id)[StartMatureProt:]
        if IncludeStart == True:
            FastaDic[id]='ATG'+FastaDic.get(id)
    else:
        Output=open('%s_wo_signalPeptide.fasta'%(Fasta), 'w')
        SeqIO.write(FastaDic.values(), Output, 'fasta')
    
    
    




