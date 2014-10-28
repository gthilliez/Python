import os

def ChosePrimers (*args):
    """Comments"""
    for arg in args:
        fh=open(arg)
        PrimerDic={}
        for UnformatedLine in fh:
            line=UnformatedLine.strip().split()
            PrimerName=line[0]
            if PrimerName in PrimerDic:
                PrimerDic.get(PrimerName).append(line)
            else:
                PrimerDic[PrimerName]=[line]
        else:
            PrimerDicSet=PrimerDic.copy()
            for Key in PrimerDicSet:
                PrimerDicSet[Key]=set([element[1]
                    for element in PrimerDic.get(Key)])
            else:
                PairDic={(KeyA, KeyB): PrimerDicSet.get(KeyA)&PrimerDicSet.get(KeyB)
                for KeyA in PrimerDicSet
                for KeyB in PrimerDicSet
                if KeyA!=KeyB}
    return PairDic





os.chdir('D:\Databases\Genomes_sequences') #
TestFH='newprimersNAC1Cluster20140408.txtBLAST_transcript20140408.txt'
DicToWrite=ChosePrimers(TestFH)

fout=open('TestSummaryNac1_newprimers.csv','w')
for k in DicToWrite:
    if len(DicToWrite.get(k))!=0:
        print>>fout, "%s,%s" %(','.join(k),','.join(DicToWrite.get(k)))
else:
    fout.close()

