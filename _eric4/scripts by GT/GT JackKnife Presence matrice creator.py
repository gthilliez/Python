import copy

Cluster_Handle=open('C:\Program Files\Cygwin\home\gt41237\dump.seq.mci.I60','rb')
StdDict={}
for line in Cluster_Handle:
    data_std=line.split()
    for entry in data_std:
        key='%s' %(entry)
        valueList=copy.copy(data_std)
        valueList.remove(entry)
        StdDict[key]=valueList
        
print '%s'%(len(StdDict))
        
PresenceListDict={}
for key in StdDict.iterkeys():
    PresenceListDict[key]=(0)
    
print '%s'%(len(PresenceListDict))
    
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
            #for entry in data:
                #AssociationListDict[key][ColumnDict.get(entry)]=AssociationListDict[key][ColumnDict.get(entry)]+1
    print 'JackKnife file %s done'%(count2)
    count2=count2-1
    

PresencePath='C:\\Users\\gt41237\\presencematrice.csv'
PresenceCSVHandle=open(PresencePath, 'wb')
for key in StdDict.iterkeys():
	print>>PresenceCSVHandle, '%s,%s' %(key,PresenceListDict.get(key))
    
PresenceCSVHandle.close()
