from sys import stdin,argv

def CreateCytoscapeInput(MCL_graph, MCLtab, output='OutputForCytoscape.csv'):
    "Comments"
    import networkx as nx
    import os
    
    G=nx.Graph()

    TableName=open(MCLtab)

    MCL_Id_Dic={line.strip().split('\t')[0]:line.strip().split('\t')[1]
                        for line in TableName}

    GraphFile=open(MCL_graph)

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

    fileout=open(output, 'w')
    for e in ListEdges:
        if None not in e:
            print>>fileout, '\t'.join(e)
        else:
            for element in e:
                if element !=None:
                    print>>fileout, element
                    
    
    fileout.close()


CreateCytoscapeInput(argv[1], argv[2])
