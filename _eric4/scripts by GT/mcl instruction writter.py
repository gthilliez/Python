from datetime import datetime
import os
import re

rgx=re.compile('\d{1,}')

now=datetime.now()
date=str(now.year)+'_'+str(now.month)+'_'+str(now.day)
Fo='D:\JackKnife_final\MCLINSTRUCTIONRXLR%s'%(date)
fileout=open(Fo, 'w')
FileDir='D:\JackKnife_final\Blast_JackKnifed_files'

for element in os.listdir(FileDir):
  if '.fasta' and'.csv' in os.path.splitext(element):
    index='%s'%(rgx.search(element).group())
    print>>fileout,  'cut -f 1,2,11 /cygdrive/d/JackKnife_final/Blast_JackKnifed_files/%s >JKRXLRDict%s.abc'%(element, date+'_'+index)
    print>>fileout, "mcxload -abc JKRXLRDict%s.abc --stream-mirror --stream-neg-log10 -stream-tf 'ceil(200)' -o JKRXLRDict%s.mci -write-tab JKRXLRDict%s.tab" %(date+'_'+index, date+'_'+index,date+'_'+index)
    print>>fileout, "mcl JKRXLRDict%s.mci -I 2"%(date+'_'+index)
    print>>fileout, "mcl JKRXLRDict%s.mci -I 4"%(date+'_'+index)
    print>>fileout, "mcl JKRXLRDict%s.mci -I 6"%(date+'_'+index)
    print>>fileout, "mcxdump -icl out.JKRXLRDict%s.mci.I20 -tabr JKRXLRDict%s.tab -o dump.JKRXLRDict%s.mci.I20"%(date+'_'+index, date+'_'+index,date+'_'+index)
    print>>fileout, "mcxdump -icl out.JKRXLRDict%s.mci.I40 -tabr JKRXLRDict%s.tab -o dump.JKRXLRDict%s.mci.I40"%(date+'_'+index, date+'_'+index,date+'_'+index)
    print>>fileout, "mcxdump -icl out.JKRXLRDict%s.mci.I60 -tabr JKRXLRDict%s.tab -o dump.JKRXLRDict%s.mci.I60"%(date+'_'+index, date+'_'+index,date+'_'+index)
fileout.close()
