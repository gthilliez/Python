from Bio import SeqIO

def GetClusterSeq(ExpressionFile, Cluster, Fasta):
    """Comments"""
    Fh_expression=open(ExpressionFile)
    ExpressedList=Fh_expression.readlines() # Expression File must be a file were each line is a single gene. name must match Cluster names
    Fhcluster=open(Cluster)
    AllClusters=Fhcluster.readlines()
    ClusterDic={}
    Fh_Fasta=open(Fasta)
    DicSeq={seq.id:seq 
    for seq in SeqIO.parse(Fh_Fasta, 'fasta')}
    for element in ExpressedList:
        TempList=[]
        for cluster in AllClusters:
            if element in cluster:
                for id in cluster:
                    if id in DicSeq:
                        TempList.append(DicSeq.get(id))
                else:
                    ClusterDic[element]=TempList
                    if len(TempList)<len(cluster):
                        print 'Error with the %s cluster; not all sequence were added to the dictionnary'%element
            else:
                print 'Error with %s; cannot be find in the cluster file'%element
    return ClusterDic



Xpression= "D:\\4 Hosts\\preliminary_work_GT\\GT_test_list_IdOnly_4host_all_values_DEG_Pete.csv"#path
Clust= 'D:\\Clustering20131212\\MCL_Output\\dump\\dump.SelfBLASTp_Combined_TrimmedPi_and_Pc_20131212_evalue1e-5.txt_MCL_.mci.I60'#path
Fast= 'D:\\Clustering20131212\\Combined_TrimmedPi_and_Pc_20131212.fasta'#path
Testdic=GetClusterSeq(Xpression, Clust, Fast)
len(Testdic)
