#Get protein spe to P. capsici
from Bio import SeqIO
#uses relax set up for more confidence on the P. cap specificity
DumpFile=open('D:\\Clustering20131212\\MCL_Output\\dump\\dump.SelfBLASTp_Combined_TrimmedPi_and_Pc_20131212_evalue1e-5.txt_MCL_.mci.I35')
PiFasta=open('D:\\Clustering20131212\\TrimmedPiProt20131212.fasta')
PcFasta=open('D:\\Clustering20131212\\TrimmedPcapsiciSeq20131212.fasta')

IdPc=[seq.id for seq in SeqIO.parse(PcFasta, 'fasta')]
IdPi=[seq.id for seq in SeqIO.parse(PiFasta, 'fasta')]

ClusterContainingPi=[]
ClusterContainingPc=[]
for cluster in DumpFile:
    for protein in cluster.strip().split('\t'):
        if protein in IdPc:
            ClusterContainingPc.append(cluster.strip()) #idem
        if protein in IdPi:
            ClusterContainingPi.append(cluster.strip()) #here see below


PcSpe=set(ClusterContainingPc)-set(ClusterContainingPi)
Temp1='\t'.join(PcSpe)
ListPcSpe=Temp1.strip.split('\t')

PcFasta.seek(0)
#correct problem with format in ListPcSpe maybe change cluster to cluster .strip.split('\'t)
Towrite=[seq for seq in SeqIO.parse(PcFasta, 'fasta') if seq.id in ListPcSpe]
len(Towrite)
output=open('C:\\Users\\gt41237\\Desktop\\PcSpe_proteins.fasta', 'w')
SeqIO.write(Towrite, output, 'fasta')
output.close()

Pcnt=open('D:\\Databases\\Phyca11_filtered_transcripts.fasta')
TowriteNt=[seq for seq in SeqIO.parse(Pcnt, 'fasta') if seq.id in ListPcSpe]
len(TowriteNt)
output2=open('C:\\Users\\gt41237\\Desktop\\PcSpe_transcripts.fasta', 'w')
SeqIO.write(TowriteNt, output2, 'fasta')
output2.close()

oldx=0
for x in range(50,len(TowriteNt),50):
    ListTowriteSub=TowriteNt[oldx:x]
    outputvar=open('C:\\Users\\gt41237\\Desktop\\PcSpe_genes\\Nt_seq_split\\PcSpe_transcripts%s_%s.fasta'%(oldx, x), 'w')
    oldx=x
    SeqIO.write(ListTowriteSub, outputvar, 'fasta')
else:
    if oldx < len(TowriteNt):
        x=len(TowriteNt)+1
        ListTowriteSub=TowriteNt[oldx:x]
        outputvar=open('C:\\Users\\gt41237\\Desktop\\PcSpe_genes\\Nt_seq_split\\PcSpe_transcripts%s_%s.fasta'%(oldx, x), 'w')
        SeqIO.write(ListTowriteSub, outputvar, 'fasta')
        outputvar.close()
