#script by G. Thilliez 2014
#The aim of this script is to write a report on a serie of MCL cluster output.
#For a series of MCL dump output, the script will get the name, the number of single prot and the number of  cluter
#It will save the report as a CSV with a header.

import os
CD=os.getcwd()
fileout=open('report.csv', 'w')
print>>fileout,  'name,evalue,Inflation_x10,Clusters,Single_prot,Total'

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


print '%s file processed successfully'%len(os.listdir(CD))
#Cluster= number of cluster (more than one protein)
#Singleton=number of single protein after Clustering
#Total=cluster+singleton
#Inflation value_x10=extention of the file wich correspond to the inflation value x 10 (eg 35 for I=3.5)
#evalue=evalue cutoff defined in the BLAST used as an input for the MCL algorythm
#name=file name

##function version
#It's better to have a function rather than a script, but here, I want the evalue and inflation to be in the report,
#the way to get inflation and evalue is totally dependent on the format of the name.
#So I cannot write a function that will universally detect this value, however if evalue and inflation value are left out, a function can be written
#see MCLdumpReport_function_20140107.py

