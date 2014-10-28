import os
from sys import stdin,argv
def ChosePrimers (*args):
    """Comments"""
    for arg in args:
        if arg!=argv[0]:
            fh=open(arg)
            HitDic={}
            for UnformatedLine in fh:
                line=UnformatedLine.strip().split()
                PrimerName=line[0]
                Hit=line[1]
                if Hit in HitDic:
                    HitDic.get(Hit).append(PrimerName)
                else:
                    HitDic[Hit]=[PrimerName]
            fout=open('Choseprimer_%s'%arg,'w')
            for k in HitDic:
                if len(HitDic.get(k))>1:
                    print>>fout, "%s\t%s" %('\t'.join(HitDic.get(k)),k)
            else:
                fout.close()


ChosePrimers(argv[1])



#os.chdir('D:\Databases\primers\Roche\BLASTResults') #
#for file in os.listdir(os.getcwd):
#    
#DicToWrite=ChosePrimers(TestFH)
#
#fout=open('TestSummaryNac1_newprimers.csv','w')
#for k in DicToWrite:
#    if len(DicToWrite.get(k))!=0:
#        print>>fout, "%s,%s" %(','.join(k),','.join(DicToWrite.get(k)))
#else:
#    fout.close()

