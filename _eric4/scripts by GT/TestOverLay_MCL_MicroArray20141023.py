#Overlay Remco's expression data and my clusters

def MakeMCLClusterDic(MCLdump):
    """Comments:
    MCLdump is a path to the MCL dump file that will be used in this analysis
    The function returns a dictionnary which can be quite big (depending on the size of the input)
    to make sure you can call back the dictionnary, assign the function call to a variable
    eg : VarDic=MakeMCLClusterDic(Mypath)
        where:  My path is a path to a MCLdump file
                    VarDic is now a Dictionnary that can be used as a normal dictionnary
    ##The dictionnary created uses the index of the cluster as a key
    ##The corresponding value is a list of all the cluster members"""
    Fh=open(MCLdump)
    MCLClusterDic={} #or is it better to use a dic?
    for indexClust, line in enumerate(Fh):
        FormatedLine=line.strip().split('\t') #how to remove the _1 or T0 at the end of the PITG number? should it be replaced now or later?
        MCLClusterDic[indexClust]=FormatedLine
    else:
        return MCLClusterDic


PathToDump='D:\\Clustering20131212\\MCL_Output\\dump\\dump.SelfBLASTp_Combined_TrimmedPi_and_Pc_20131212_evalue1e-5.txt_MCL_.mci.I60'
MCLClustDic=MakeMCLClusterDic(PathToDump)

##The dictionnary created uses the index of the cluster as a key
##The corresponding value is a list of all the cluster members
#---#
##The main problem here is to make sure the id of protein in the cluster
##will match the id of genes in the expression data. Eg PHYCAscaffold vs Phyca11 names

def MakeExpressionCluster(ExpressionFile, Header=True, ClusterCol=0, IdCol=1, sep='\t'):
    """Comments
    This function create a Dictionnary from and ExpressionFile
    ExpressionFile should be a path to a tabular file containing at least two information
    a group or cluster, and the id of the gene.
    ClusterCol (int) is the index of the column indiccating group (eg if the first column is the cluster, ClusterCol is 0)
    IdCol (int) is the index of the column indicating the gene Id (eg IdCol=1 if the gene Id is stored in column 2)
    sep is the separator used in the table. eg sep='\t' for tab delimited file (default) or sep=',' if the ExpressionFile is a csv file
    Header=True if the input file has a Header. Change it to any value if the input file doesn't have a header"""
    Fh=open(ExpressionFile)
    ExpressionDic={}
    if Header==True:
        HeadLine=Fh.readline().strip().split(sep)
    for line in Fh:
        FormatedLine=line.strip().split(sep)
        ExpCluster=FormatedLine[ClusterCol]
        GeneId=FormatedLine[IdCol]
        ExpressionDic[GeneId]=ExpCluster
    else:
        return ExpressionDic



PathToExpFile='D:\\4 Hosts\\exp_clusters.txt'
ExpDic=MakeExpressionCluster(PathToExpFile)
##ExpDic should be a dictionnary were the key is a cluster

def CompareMCLandExpDic(MCLDic, ExpressionDic):
    """Comments
    """
    for Key in MCLDic.iterkeys():
        for GeneId in MCLDic.get(Key):
            
            if 'PcRxLR' in GeneId: #Lines were added to correct name in the MCL clustering
                GeneId2=GeneId.replace('_1', '') #here correct PcRxLR names to remove the _1 at the end
            elif 'Phyca11' in GeneId: #here convert long Phyca11 names in "Phyca11_####" like in Remco's file
                GeneId2='Phyca11_'+GeneId.split('|')[2]
            else:
                GeneId2=GeneId
                
            if GeneId2 in ExpressionDic:
                MCLDic.get(Key).remove(GeneId)
                MCLDic.get(Key).append(GeneId+'expCluster'+str(ExpressionDic.get(GeneId2)))
    else:
        return MCLDic


MCLandExpressionDic=CompareMCLandExpDic(MCLClustDic, ExpDic)

#problem with the PcRxLR_1 and Phyca names ## was fixed with quick and dirty modifications
output=open('D:\\4 Hosts\\NewCluster.txt', 'w')
for k in MCLandExpressionDic:
    print>>output,  '%s'%'\t'.join(MCLandExpressionDic.get(k))
else:
    output.close()
#could modify it to count the number of gene found in micro-array table and not in cluster
#or found in MCL cluster but not expressed
#and other summaries
