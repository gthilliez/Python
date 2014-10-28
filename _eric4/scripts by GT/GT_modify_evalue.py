#script to change the evalue of a blast. 

import re

rgx=re.compile("\'|\[|\]")
FileHandle=open('C:\Users\gt41237\Clustering_GT_2013\Self_blasts\RxLRs only\WOselfhitselfblastPiPcTruncRxLR', 'r')
fileout=open('C:\Users\gt41237\Clustering_GT_2013\Self_blasts\RxLRs only\WOselfhitselfblastPiPcTruncRxLR_corrected_evalue', 'w')
for line in FileHandle:
    L=line.split()
    if len(L)>0:
        e_old='%e'%(float(L[10]))
        e_new=(float(e_old)/122209)*13719588 ##122209 and 13719588 are hardcpded db size, would be better to change them to variable
        if e_new<1e-5: #discar all the evalue superior to 1e-5
            L[10]=e_new
            print>>fileout,  rgx.sub('', str(L))
            
fileout.close()
