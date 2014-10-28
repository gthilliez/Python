#Fh=open('D:\\Clustering20131212\\BLAST\\SelfBLASTp_Combined_TrimmedPi_and_Pc_20131212_evalue1e-5.txt')
Fh=open('D:\\Clustering20131212\\MCL_Output\\dump\\dump.SelfBLASTp_Combined_TrimmedPi_and_Pc_20131212_evalue1e-5.txt_MCL_.mci.I60')
ListHits=[]
for line in Fh:
    if '112277' in line:
        ListHits.append(line)


SharedPc=[]
for ele in ListHits:
    if 'PcRxLR' in ele or 'Phyca' in ele:
        SharedPc.append(ele)


len(SharedPc)


