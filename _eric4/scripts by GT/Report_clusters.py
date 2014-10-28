import os
CD=os.getcwd()
fileout=open('report.csv', 'w')
print>>fileout,  ('name', 'evalue', 'Inflation_x10', 'Clusters', 'Single_prot', 'Total')

for file in os.listdir(CD):
    fh=open(file, 'r')
    Cluster=0
    Singleton=0
    name=fh.name
    evalue=fh.name.split('.')[1].split('evalue')[-1]
    Inflation_x10=fh.name.split('.')[-1]
    for line in fh:
        Length=len(line.strip().split('\t'))
        if Length>1:
            Cluster=Cluster+1
        else:
            Singleton=Singleton+1
    Total=Cluster+Singleton
    print>>fileout, ('%s, %s, %s, %s,  %s, %s')%(name, evalue, Inflation_x10, Cluster, Singleton, Total)
    
