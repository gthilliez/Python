
from sys import stdin, argv
import os

def Function_compileXLS(folder, output):
    """COMMENTs"""

    previouscol1=0
    fileout=open(output,'w')##to define
    ListCol2=[]
    for index, file in enumerate(os.listdir(folder)):
        fh=open(os.path.join(folder, file))
        header=fh.readline()
        if index==0:
            print>>fileout,  header.strip()
        tempListCol2=[]
        for unformatedline in fh:
            Line=unformatedline.strip().split('\t')
            Line[0]=int(previouscol1)+1
            previouscol1=Line[0]
            if float(Line[1]) in ListCol2:
                Line[1]=str(max(ListCol2)+1)
            else:
                tempListCol2.append(float(Line[1]))
            print>>fileout, '\t'.join(str(e) for e in Line)
        else:
            ListCol2=tempListCol2+ListCol2
    else:
        fileout.close()


Function_compileXLS(argv[1], argv[2])
