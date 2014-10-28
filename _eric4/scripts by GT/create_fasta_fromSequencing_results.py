import os


SeqDir='D:\Y2H\PITG_09218\\results_2-6-14_run28'
os.chdir(SeqDir)
Fileout=open('OutputFastaPITG_09218.fasta', 'w')
for file in os.listdir(SeqDir):
    if '.seq' in file:
        fh=open(file)
        id=fh.name
        seq=fh.read().replace('\n', '')
        print>>Fileout,  '>%s'%id
        print>>Fileout,  '%s'%seq


Fileout.close()
