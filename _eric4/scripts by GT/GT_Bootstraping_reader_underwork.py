Run=raw_input('Do you want to run the cluster reader script? (y/n): ')
while Run =='y':
    StdPath=raw_input('Enter the path for the standard Clusters: ')
    StdFile=open(StdPath, 'rb')
    BootstrapPath=raw_input('Enter the path for the Bootstraped Clusters: ')
    BootstrapFile=open(BootstrapPath, 'rb')
    import re
    
    
    StdDict={}
    for line in StdFile:
        data_std=line.split()
        for entry in data_std:
            EntrySplit_Std=entry.split('_')
            if 'PITG' in EntrySplit_Std:
                Key_Std="%s_%s"%(EntrySplit_Std[0], EntrySplit_Std[1])
                StdDict[Key_Std]=data_std
            else:
                Key_Std="%s"%(EntrySplit_Std[0])
                StdDict[Key_Std]=data_std
    
    for key in StdDict:
        Valuelist=[]
        for value in StdDict.get(key):
            SplitValue=value.split('_')
            if 'PITG' in SplitValue:
                NewValue='%s_%s'%(SplitValue[0], SplitValue[1])
            else:
                NewValue='%s'%(SplitValue[0])
            if NewValue != key and NewValue not in Valuelist:
                Valuelist.append(NewValue)
                StdDict[key]=Valuelist
    
    BootstrapDict={}
    for line in BootstrapFile:
        data_Bootstrap=line.split()
        for entry in data_Bootstrap:
            EntrySplit=entry.split('_')
            Searchable_EntrySplit='%s'%(EntrySplit)
            Pcpresence=0
            if 'PITG' in EntrySplit:
                Key_Bootstrap="%s_%s"%(EntrySplit[0], EntrySplit[1])
                BootstrapDict[Key_Bootstrap]=data_Bootstrap
            else:
                Key_Bootstrap="%s"%(EntrySplit[0])
                BootstrapDict[Key_Bootstrap]=data_Bootstrap
    
    for key in BootstrapDict:
        Valuelist=[]
        for value in BootstrapDict.get(key):
            SplitValue=value.split('_')
            if 'PITG' in SplitValue:
                NewValue='%s_%s'%(SplitValue[0], SplitValue[1])
            else:
                NewValue='%s'%(SplitValue[0])
            if NewValue != key and NewValue not in Valuelist:
                Valuelist.append(NewValue)
                #print Valuelist
            BootstrapDict[key]=Valuelist
                
    
    
    CommonsDict={}
    FalsePositiveDict={}
    LackingInBootstrapDict={}
    FalseNegativeDict={}
    ValueNIBDict={}
    #Dictionaries to store the data
    fileoutpath=raw_input('choose the path to which the data will be store: ')
    fileout=open(fileoutpath, 'wb')
    print>>fileout,  'Key, Key_In_Bootstrap, length_Standard_Cluster,Length_Bootstrap_cluster, length_common_Std-Bootstrap,length_false_negatives,length_false_positives,length_value_not_in_bootstrap '
    
    for key in StdDict:
        if key in BootstrapDict:
            LBD=len(BootstrapDict.get(key))
            BootstrapSet=set(BootstrapDict.get(key))
            StdSet=set(StdDict.get(key))
            commons=BootstrapSet.intersection(StdSet)
            if len(commons)!=0:
                CommonsDict[key]=commons
            if key in CommonsDict:
                LCD=len(CommonsDict.get(key))
            else:
                LCD=0
            FalseNegative=StdSet.difference(BootstrapSet)
            FalseNegList=list(FalseNegative)
            count=len(FalseNegList)
            count=count-1
            Neglist=[]
            ValueNIBList=[]
            while count!=-1:
                if FalseNegList[count] in BootstrapDict:
                    Neglist.append(FalseNegList[count])
                    FalseNegativeDict[key]=Neglist
                    count=count-1
                else:
                    ValueNIBList.append(FalseNegList[count])
                    ValueNIBDict[key]=ValueNIBList
                    count=count-1
            if key in ValueNIBDict:
                LVNIB=len(ValueNIBDict.get(key))
            else:
                LVNIB=0
            if key in FalseNegativeDict:
                LFN=len(FalseNegativeDict.get(key))
            else:
                LFN=0
            FalsePositives=BootstrapSet.difference(StdSet)
            if len(FalsePositives)!=0:
                FalsePositiveDict[key]=FalsePositives
            if key in FalsePositiveDict:
                LFP=len(FalsePositiveDict.get(key))
            else:
                LFP=0
        else:
            LackingInBootstrapDict[key]='%s not in the Bootstrap' %(key)
            LBD=0
            LCD=0
            LFP=0
            LFN=0
            LVNIB=0
        if key in LackingInBootstrapDict:
            IdInBD=0
        else:
            IdInBD=1
        print>>fileout,  '%s,%s,%s,%s,%s,%s,%s,%s'%(key,IdInBD,  len(StdDict.get(key)), LBD, LCD, LFN, LFP, LVNIB)
        
    print>>fileout,  'each line represente the association of one protein (key) with the others'
    print>>fileout, 'one line does not represent one cluster'
    print>>fileout, 'Key_In_Bootstrap indicate if the key considered is present in the bootstrap dict (1) or not (0)'
    print>>fileout, 'length_Standard_Cluster give the size of the standard cluster whereas Length_Bootstrap_cluster give the length of the Bootstrap cluster associated with the given key'
    print>>fileout, 'length_common_Std-Bootstrap give the number of shared member between the Standard and Bootstrap cluster'
    print>>fileout, 'length_false_negatives give the number of value present in the bootstrap dict, associated with the key in the Standard dictionary but in a different cluster in the Bootstrap'
    print>>fileout, 'length_false_positives give the number of value present in both Bootstrap and Standard dict, not associated with the key in the StdDict but associated with the key in the Bootstrap'
    print>>fileout, 'length_value_not_in_bootstrap give length of the Value not in boostrap dictionary (for a given key, tell if one of the value associated with the key in the Std Dict is absent from the bootstrap) '
    fileout.close()
    
    Run=raw_input('Do you want to re run the script on other files? (y/n): ')
    #LBD give the length of the Bootstrap Dictionnary for a given key (if available)
    #LCD give the length of the Common dictionnary (common Bootstrap/Strandard) for a given key (if available)
    #LFN give the length of the false negative dictionnary for a given key if available (value present in the bootstrap dict, associated with the key in the Standard dictionary but in a different cluster in the Bootstrap)
    #LFP give the length of false positive dictionnary for a given key if available (value present in both Bootstrap and Standard dict, not associated with the key in the StdDict but associated with the key in the Bootstrap)
    #LVNIB give length of the Value not in boostrap dictionary (for a given key, tell if one of the value associated with the key in the Std Dict is absent from the bootstrap)
    #IdInBD just tell if the key is present in the bootstrap dictionary (1) or not (0)
    
    ##need to add the columns names
