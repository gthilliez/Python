import os
import csv
os.chdir('D:\Clustering20131212\GALAXY_RBBH')
fh=open('Galaxy11-[RBH_results_50__cov_70__id_TrimmedPiProt20131212_vs_TrimmedPcapsiciProt20131212].tabular')

def DicGalaxyRBBH(RBBHTab, Dic='default', Header=True, col1=0, col2=1):
    """Create a Dictionnary containing query as keys and RBBH as value
    This function uses the csv module (imported by the function)
    It reads tabular file, guess the csv dialect associated to it and 
    create a dictionnary where col1= key and col2=associated value.
    
    First Arg must be an open file (RBBH tabular output from galaxy) or a path
    
    Second argument is optional, if not defined it create a dictionnary
        in that case use the function like this : NewDic=DicGalaxyRBBH(RBBHTab)
        NewDic will be a Dictionnary.
        if you want to update a Dictionnary : DicGalaxyRBBH(RBBHTab,DicToUpdate)
        DicToUpdate will be updated by the function. 
        If key are redundant in the DicToUpdate before the function and in the RBBHTab, then the key will be overwriten.
    
    Third argument is Header. if set as True, the first line will be skipped (default) if set as False, the first line wont be skipped
    
    Fourth Argument is the position of col1, by default it is index 0 (integrer)
    
    Fifth Argument is the position of col2, by default it is index 1 (integrer)"""
    import csv
    if type(col1)!=type(0) and type(col2)!=type(0):
        print 'error, col1 and col2 must be intergrer'
    if type(RBBHTab)==type('string'):
        RBBHTab=open(RBBHTab)
    elif 'file' not in str(type(RBBHTab)):
        print 'error, please provide an open file or a path'
    RBBHTab.seek(0)
    dialect=csv.Sniffer().sniff(RBBHTab.read(2048))
    reader=csv.reader(RBBHTab, dialect)
    RBBHTab.seek(0)
    if Header==True:
        SkipHeader=reader.next()
    if Dic=='default':
        Dic={line[col1]:line[col2]
             for line in reader}
        return Dic
    else:
        for line in reader:
            Dic[line[col1]]=line[col2]
