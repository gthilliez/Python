import os
import csv

def CreateEffectorDic(folder, header=True, PhycaColumn=0):
    """Create a Dictionnary of Dictionnary
    GeneralDic Keys = name of CSV files in folder
    CSV file in folder should correspond to different expression profile
    eg ClassI.csv and ClassII.csv
    GeneralDic keys = ClassI  and ClassII
    value for ClassI = file dic
    file dic key = PhycaColumn (containing the Phycascaffold Id; by default is 0)
    value for a key is the name of the file and the line associated with Phycascaffold id
    return a dictionnary.
    to call the function : Variable=CreateEffectorDic(folder)
    with folder being a path to a folder containing only the CSV of interest
    Variable becomes a dictionnary"""
    import os
    import csv
    olddir=os.getcwd()
    os.chdir(folder)
    GeneralDic={}
    for file in os.listdir(folder):
        filehandle=open(file)
        dialect=csv.Sniffer().sniff(filehandle.read(2048))
        reader=csv.reader(filehandle, dialect)
        filehandle.seek(0)
        if header==True:
            header=reader.next()
        filedic={line[PhycaColumn]:[file, line]
                    for line in reader}
        GeneralDic[file]=filedic
    else:
        os.chdir(olddir)
        return GeneralDic



ExpressionTableEffector=CreateEffectorDic('D:\CLUSTER_RXLR20140309\ExpressionTable\CSVFiles')
Phyca_Pcfh=open('D:\CLUSTER_RXLR20140309\Sorted_Phyca11_Phycascaffold_PcRxLR_names.csv')

def CreateEffectorDic2(table, header=True, KeyColumn=0, ValueColumn=1):
    """Create a dictionnary of effector with their Phycascaffold 11 name
    uses a table containing Phycascaffold name and PcRXLR name (example Sorted_Phyca11_Phycascaffold_PcRxLR_names.csv)
    Dictionnary created key = Phycascaffold name ; value = PcRXLR name
    table is the table containing Phycascaffold and PcRXLR name
    header is True by default which means it will skip the first line of the table to create the dictionnary
    KeyColumn is the position of the name to be use as a Key (default = 0)
    ValueColumn is the position of the name to be use as a Value (default = 1)
    to use the function : Variable=CreateEffectorDic2(table)
    additional parameter (header; KeyColumn ValueColumn) can be changed"""
    import os
    import csv
    dialect=csv.Sniffer().sniff(table.read(2048))
    reader=csv.reader(table, dialect)
    table.seek(0)
    if header==True:
        header=reader.next()
    dic={line[KeyColumn]:line[ValueColumn]
            for line in reader}
    return dic


PcPhycaDic=CreateEffectorDic2(Phyca_Pcfh, KeyColumn=1, ValueColumn=0)

RXLRDic={}
for KeyA in ExpressionTableEffector:
    if KeyA!='TableS9_CSV.csv':
        for k in PcPhycaDic:
            if k in ExpressionTableEffector.get(KeyA):
                Pcname=PcPhycaDic.get(k)
                RXLRDic[Pcname]=[Pcname, k, (KeyA.split('.')[0])]


for KeyB in PcPhycaDic:
    Pcname=PcPhycaDic.get(KeyB)
    if Pcname not in RXLRDic:
        if KeyB in ExpressionTableEffector.get('TableS9_CSV.csv'):
            RXLRDic[Pcname]=[Pcname, k,'S9']
        else:
            RXLRDic[Pcname]=[Pcname, k,'NE']



SpeciesSpeClusterFolder='D:\CLUSTER_RXLR20140309\SpeciesCluster\WaitingList'

def createRXLRTable (RXLRDic, ClusterFolder, Outfile='OutputFileCreateRXLRTable.csv'):
    '''Comments'''
    import os
    OldFolder=os.getcwd()
    os.chdir(ClusterFolder)
    for file in os.listdir(ClusterFolder):
        fh=open(file)
        for line in fh:
            cluster=line.strip().split('\t')
            for protid in cluster:
                if protid.replace('_1', '') in RXLRDic:
                    RXLRDic.get(protid.replace('_1', '')).append(fh.name)
    else:
        Fh_output=open(Outfile, 'w')
        for k in RXLRDic:
            print>>Fh_output,  ','.join(RXLRDic.get(k))
        else:
            Fh_output.close()
            os.chdir(OldFolder)



createRXLRTable(RXLRDic, SpeciesSpeClusterFolder )
