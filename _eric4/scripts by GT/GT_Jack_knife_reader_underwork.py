import copy
import re
regex1=re.compile("\[|'|\]|\"")

#import numpy as np
Cluster_Handle=open('C:\Program Files\Cygwin\home\gt41237\dump.seq.mci.I60','rb')
StdDict={}
for line in Cluster_Handle:
    data_std=line.split()
    for entry in data_std:
        key='%s' %(entry)
        valueList=copy.copy(data_std)
        valueList.remove(entry)
        StdDict[key]=valueList

#Lines above creates a dictionary, key= one protein seq, value= associated proteins in the cluster
PresenceListDict={}
AssociationListDict={}
###

#lines above creates dictionaries containing list, will be use to store number of time a given protein is present in the 50 JackKnife files for PresenceArrayDict
#and number of time it is associated with a given protein (key) for AssociationListDict

for key in StdDict.iterkeys():
    PresenceListDict[key]=(0)
    AssociationListDict[key]=[0]*38124
    
ColumnDict={}
ColumnCount=0
for key in StdDict.iterkeys():
    ColumnDict[key]=ColumnCount
    ColumnCount=ColumnCount+1
#Lines above give a column position to all the proteins present in the clustering.
#Position will be use in AssociationArrayDict

count2=50
while int(count2) > 0:
    JKfilepath='C:\Users\gt41237\JackKnives\MCL_Output\dump.JKDict%s.mci.I60'%(count2)
    JK_Handle=open(JKfilepath, 'rb') 
    JK_dict={}
    for line in JK_Handle:
        data_JK=line.split()
        for entry in data_JK:
            key='%s'%(entry)
            valueList2=copy.copy(data_JK)
            valueList2.remove(entry)
            JK_dict[key]=valueList2
    for key in StdDict.iterkeys():
        if key in JK_dict:
            data=JK_dict.get(key)
            PresenceListDict[key]=PresenceListDict[key]+1 #probleme
            for entry in data:
                AssociationListDict[key][ColumnDict.get(entry)]=AssociationListDict[key][ColumnDict.get(entry)]+1
    count2=count2-1
## change the line mark with one hash key


AssociationPath='C:\\Users\\gt41237\\associationmatrice.csv'
AssociationCSVHandle=open(AssociationPath, 'wb')
print>>AssociationCSVHandle,  '%s,%s,%s' %(' ',' ', StdDict.keys()) #space, space, 1 to 38124'
#print>>AssociationCSVHandle, '%s' ()#space space, effector name 1 to 38128
count=0
for key in StdDict.iterkeys():
    #keyid='%s'%(ColumnDict.get(key))
    #value='%s'%(AssociationListDict.get(key))
    print>>AssociationCSVHandle,  '%s,%s,%s' %(count, ColumnDict.get(key), regex1.sub('',AssociationListDict.get(key))) # effector number, effector name, value associated
    count=count+1
    
RatioDict=AssociationListDict.copy()
for key in StdDict.iterkeys():
    for key2 in ColumnDict.iterkeys():
        RatioDict[key][ColumnDict.get(key2)]=RatioDict[key][ColumnDict.get(key2)]/PresenceListDict[key2]
        
RatioPath='C:\\Users\\gt41237\\ratiomatrice.csv'
RatioCSVHandle=open(RatioPath, 'wb')
print>>RatioCSVHandle,  '%s,%s,%s' %(' ',' ', StdDict.keys())
count=0
for key in StdDict.iterkeys():
    print>>RatioCSVHandle,  '%s,%s,%s' %(count, ColumnDict.get(key), RatioDict.get(key))
    count=count+1
