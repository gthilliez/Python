import networkx as nx
import os

G=nx.Graph()

#open output graph
#also need numercal value == id table
##Use of a dictionnary?

TableName=open('SelfBLASTp_Combined_TrimmedPi_and_Pc_20131212_evalue1e-30.txt_MCL_.tab')

MCL_Id_Dic={line.strip().split('\t')[0]:line.strip().split('\t')[1]
                    for line in TableName}

GraphFile=open('OutputGraph-SelfBLASTp_Combined_TrimmedPi_and_Pc_20131212_evalue1e-30.txt_MCL_.I65')
##problem with header

AllCluster=[]
for line in GraphFile:
    SplitLine=line.strip().split(' ')
    ClusterList=[]
    for element in SplitLine:
        node=element.split(':')[0]
        ClusterList.append(MCL_Id_Dic.get(node))
    else:
        AllCluster.append(ClusterList)


G.add_nodes_from(MCL_Id_Dic.values())

ListEdges=[(Cluster[0], id)
                for Cluster in AllCluster
                for id in Cluster
                if Cluster[0]!=id]


BLAST=open('SelfBLASTp_Combined_TrimmedPi_and_Pc_20131212_evalue1e-30.25col.txt')#BLAST with evalue cutoff of 1e-30
Dic={}
for line in BLAST:
    FormatLine=line.strip().split('\t')
    Query=FormatLine[0]
    Hit=FormatLine[1]
    Dic[(Query, Hit)]=line.strip().split('\t')

#store all BLAST result in a Dictionary with key = (Query,Hit) value=BLAST result
for Edge in G.edges():
    if Edge in Dic:
        
        if len(Dic.get(Edge))==24: ##modify because the last column is not there --------------------------------------------------------------------=========================[[[[[[[[[[[[[[[[[[[[[[[[[[[[
            qend=float(Dic.get(Edge)[7])
            qstart=float(Dic.get(Edge)[6])
            qlen=float(Dic.get(Edge)[22])
            PercentCoverage=((qend-qstart+1)*100)/qlen
            Dic.get(Edge).append(PercentCoverage)
            G.edge[Edge[0]][Edge[1]]['%s'%('_hit_'.join(Edge))]=Dic.get(Edge)
        else:
            print 'unexpected BLAST dictionnary value length for %s'%','.join(Edge)
    else:
        print 'no Hit found between %s'%' and '.join(Edge)
    if Edge[::-1] in Dic:
        if len(Dic.get(Edge[::-1]))==25:
            qend=float(Dic.get(Edge[::-1])[7])
            qstart=float(Dic.get(Edge[::-1])[6])
            qlen=float(Dic.get(Edge[::-1])[22])
            PercentCoverage=((qend-qstart+1)*100)/qlen
            Dic.get(Edge[::-1]).append(PercentCoverage)
            G.edge[Edge[0]][Edge[1]]['%s'%('_hit_'.join(Edge[::-1]))]=Dic.get(Edge[::-1])
    else:
        print 'no Hit found between %s'%' and '.join(Edge[::-1])

fileout=open('OutputGraphForCytoscape.csv', 'w')
for k in Dic.iterkeys():
    print>>fileout,  ",".join(Dic.get(k))
    
