import re
from Bio.SeqUtils import quick_FASTA_reader

regex_PITG=re.compile('PITG_.....')
regex_PcRxLR=re.compile('PcRxLR...')
regex_Phyca11=re.compile('Phyca11......')
#filepath='C:\Program Files\Cygwin\home\gt41237\dump.seq.mci.I60' 
##replaced by a raw input
filepath=raw_input('Enter the file path of the MCL clustering dump file : ')
filehandle=open(filepath,'rb')


##use another strategy, create a list that contain only the RxLR_PITG and another one containing the non RxLR_PITG, use those list to create dictionaries
allPITG={}
NonRxLR_PITG={}
import_All_PITG=raw_input('Enter input filepath of the P. infestans predicted protein sequences: ') 
entries_All_PITG=quick_FASTA_reader(import_All_PITG)
for name, seq in entries_All_PITG:
    try:
        temp_PITG= re.search(regex_PITG, name) #search for the PITG_xxxxxx name where x is a number
        PITG_name = temp_PITG.group() 
        print("%s"%(PITG_name)) # to see if everything is working fine
        allPITG[PITG_name] = seq
        NonRxLR_PITG[PITG_name] = seq
    except: #this line is their to avoid crash when the program encounter a non RxLR effector (effector that does not match with the definition given in Whisson et al 2007)
        print('%s, does not have a PITG standard name')%(name) #give the name of the non RxLR in the input file
        continue #if continue is not there, the for loop would start from the beginning again

PITG_RxLR={}
import_RxLR_PITG=raw_input('Enter input filepath of the P. infestans predicted RxLR: ') 
entries_RxLR_PITG=quick_FASTA_reader(import_RxLR_PITG)
for name, seq in entries_RxLR_PITG:
    try:
        temp_PITG= re.search(regex_PITG, name) #search for the PITG_xxxxxx name where x is a number
        PITG_name = temp_PITG.group() 
        print("%s"%(PITG_name)) # to see if everything is working fine
        PITG_RxLR[PITG_name] = seq
    except: #this line is their to avoid crash when the program encounter a non RxLR effector (effector that does not match with the definition given in Whisson et al 2007)
        print('%s, does not have a PITG standard name')%(name) #give the name of the non RxLR in the input file
        continue #if continue is not there, the for loop would start from the beginning again

for Key1 in allPITG:
    for Key2 in PITG_RxLR:
        if Key1==Key2:
            NonRxLR_PITG.pop(Key1)

##PITG_RxLR contain all the RxLR from P. infestans
##NonRxLR_PITG contain all the other protein from P. infestans
##allPITG contain both RxLR and non RxLR proteins from P. infestans
Cluster_PITG_RxLR={}
Cluster_PITG_NonRxLR={}
PiRxLR_sizedict={}
PiNonRxLR_sizedict={}
previousClustername_NonRxLR='none'
previousClustername_RxLR='none'
countPiRxLR=0
ClusterPITGRxLRnb={}
countPiNonRxLR=0
ClusterPITGNonRxLRnb={}

for row in filehandle:
    data=row.split()
    firstname='%s'%(data[0])
    sizecluster='%s'%(len(data))
    Clustername='%s_%s'%(firstname, sizecluster)  
    #try:
        #PITG_finder=re.search(regex_PITG, row)
        #PITG_group='%s'%(PITG_finder.group())
        
    for key_1 in PITG_RxLR:
        PITGKEY1NAME='%s'%(key_1)
          
        if PITGKEY1NAME in row:
            Cluster_PITG_RxLR[Clustername]=data  
            #sizecluster_PiRxLR='%s'%(len(data))
            if Clustername==previousClustername_RxLR:
                countPiRxLR=countPiRxLR+1
            else:
                countPiRxLR=1
                
            if sizecluster not in PiRxLR_sizedict:
                PiRxLR_sizedict[sizecluster]=1
            else:
                if Clustername != previousClustername_RxLR:
                    newvaluePiRxLR=PiRxLR_sizedict.get(sizecluster)+1
                    print 'RxLR new value for %s is %s'%(sizecluster, newvaluePiRxLR)
                    PiRxLR_sizedict[sizecluster]=newvaluePiRxLR
                    #countPiRxLR=1
                #else:
                    #countPiRxLR=countPiRxLR+1
            
            ClusterPITGRxLRnb[Clustername]=countPiRxLR
            print 'There is a P. infestans RxLR in %s'%(Clustername)
            previousClustername_RxLR=Clustername

    for key_2 in NonRxLR_PITG:
        NoNRxLXKEY2NAME='%s'%(key_2)
            
        if NoNRxLXKEY2NAME in row:
            #sizecluster_PiNonRxLR='%s'%(len(data))
            Cluster_PITG_NonRxLR[Clustername]=data
            if Clustername==previousClustername_NonRxLR:
                countPiNonRxLR=countPiNonRxLR+1
            else:
                countPiNonRxLR=1
                
            if sizecluster not in PiNonRxLR_sizedict:
                PiNonRxLR_sizedict[sizecluster]=1
            else:
                if Clustername != previousClustername_NonRxLR:
                    newvalue=PiNonRxLR_sizedict.get(sizecluster)+1
                    print 'new value for %s is %s'%(sizecluster, newvalue)
                    PiNonRxLR_sizedict[sizecluster]=newvalue
                    #countPiNonRxLR=1
                #else:
                    #countPiNonRxLR=countPiNonRxLR+1
                
            ClusterPITGNonRxLRnb[Clustername]=countPiNonRxLR
            print 'There is a P. infestans protein seq in %s'%(Clustername)
            previousClustername_NonRxLR=Clustername

##Those lines aboves can detect if a PITG protein is in the cluster but it doesn't make a difference between RxLR and non-RxLR protein from P. infestans
##need to write lines to count the number of RxLR or non RxLR per cluster
##--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
filehandle=open(filepath,'rb')
count=1
PcRxLR_dict={}
PcRxLR_sizedict={}
NbPcRxLRdict={}
previous_sizecluster='none'
for row in filehandle:
    data=row.split()
    firstname='%s'%(data[0])
    Counting_PcRxLR=re.findall(regex_PcRxLR, row)
    Nb_RxLR='%s'%(len(Counting_PcRxLR))
    sizecluster='%s'%(len(data))
    Clustername='%s_%s'%(firstname, sizecluster)
    try:
        PcRxLR_finder=re.search(regex_PcRxLR, row)
        PcRxLR_group='%s'%(PcRxLR_finder.group())
        #print data, len(data)
        if PcRxLR_group in row:
            print 'There is a P. capsici effector seq in %s'%(Clustername)
            PcRxLR_dict[Clustername]=data
            
            NbPcRxLRdict[Clustername]=Nb_RxLR
            if sizecluster==previous_sizecluster:
                count=count+1
            else:
                count=1
            PcRxLR_sizedict[sizecluster]=count
            previous_sizecluster=sizecluster
    except:
        continue
##those lines aboves can detect if a PcRxLR (effector from P. capsici) is present in a cluster
##PcRxLR dict give the number of cluster of each size containing at least 1 PcRxLR, in the key their is also the number of PcRxLR seq in the cluster.
##I also need to cross reference it with the number of cluster containing PITG_effectors.
filehandle=open(filepath,'rb')
Phyca11_dict={}
NbPhyca11dict={}
Phyca11_sizedict={}
count_Phyca=0
previous_sizecluster_phyca='none'
PhycaPreviousClustername='none'
for row in filehandle:
    data=row.split()
    firstname='%s'%(data[0])
    Counting_Phyca11=re.findall(regex_Phyca11, row)
    Nb_Phyca11='%s'%(len(Counting_Phyca11))
    sizecluster='%s'%(len(data))
    Clustername='%s_%s'%(firstname, sizecluster)
    try:
        Phyca11finder=re.search(regex_Phyca11, row)
        Phyca11group='%s'%(Phyca11finder.group())
        if Phyca11group in row:
            print 'There is a Phyca11 non RxLR seq in %s'%(Clustername)
            Phyca11_dict[Clustername]=data
            Phyca11_sizedict[sizecluster]=count_Phyca
            NbPhyca11dict[Clustername]=Nb_Phyca11
            if sizecluster==previous_sizecluster_phyca:
                    if Clustername!=PhycaPreviousClustername:
                        count_Phyca=count_Phyca+1
                    else:
                        count_Phyca=1
            Phyca11_sizedict[sizecluster]=count_Phyca
            previous_sizecluster_phyca=sizecluster
            PhycaPreviousClustername=Clustername
    except:
        continue

##Dictonaries is always the way to go !
filehandle=open(filepath,'rb')
Outputdict={}
for row in filehandle:
    data=row.split()
    firstname='%s'%(data[0])
    sizecluster='%s'%(len(data))
    Clustername='%s_%s'%(firstname, sizecluster)
    if Clustername in NbPcRxLRdict:
        NbPcRxLRvalue='%s'%(NbPcRxLRdict.get(Clustername))
    else:
        NbPcRxLRvalue=0
    if Clustername in NbPhyca11dict:
        NbPhyca11dictvalue='%s'%(NbPhyca11dict.get(Clustername))
    else:
        NbPhyca11dictvalue=0
    if Clustername in ClusterPITGRxLRnb:
        ClusterPITGRxLRnbvalue='%s'%(ClusterPITGRxLRnb.get(Clustername))
    else:
        ClusterPITGRxLRnbvalue=0
    if Clustername in ClusterPITGNonRxLRnb:
        ClusterPITGNonRxLRnbvalue='%s'%(ClusterPITGNonRxLRnb.get(Clustername))
    else:
        ClusterPITGNonRxLRnbvalue=0
    Outputdict[Clustername]=sizecluster, NbPcRxLRvalue,NbPhyca11dictvalue,ClusterPITGRxLRnbvalue,ClusterPITGNonRxLRnbvalue,data
    
outfile=raw_input('enter the file path to the output file:')
fileouttable=open(outfile, 'wb')
print>>fileouttable,  'Cluster_name,Cluster_size,Nb_PcRxLR,Nb_PcNonRxLR,Nb_PiRxLR,Nb_PiNonRxLR,members'

for key in Outputdict:
    print>>fileouttable, '%s,%s,%s,%s,%s,%s,%s'%(key,Outputdict.get(key)[0],Outputdict.get(key)[1],Outputdict.get(key)[2],Outputdict.get(key)[3],Outputdict.get(key)[4],Outputdict.get(key)[5])
fileouttable.close()
