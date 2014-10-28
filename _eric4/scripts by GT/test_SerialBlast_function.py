import subprocess
import os
import re
from multiprocessing import Process,  Pool

#input file must be fasta format, the rgx is here to distinguish between the fasta file and the blastdb files
rgx=re.compile('fasta$')
FileDir='C:\Users\gt41237\Cluster_on_RxLRs_only\JackKnife_dict_Pi_Pc_Ps_EER_trunc'
OutDir='C:\Users\gt41237\Cluster_on_RxLRs_only'
L=[]
for element in os.listdir(FileDir):
    if rgx.search(element):
        L.append(element)
        
def SerialBlast(FileDir, OutDir):
  #for element in os.listdir(FileDir):
  FDir=FileDir
  ODir=OutDir
  for element in os.listdir(FDir):
    if rgx.search(element):
      print element
      filepath=FDir+'\\'+element
      fileoutpath=ODir+'\\'+'SelfBLASTp'+element+'.csv'
      testsub=subprocess.Popen(['blastp', '-query',filepath, '-db', filepath, '-evalue', '1e-5','-outfmt', '6','-out', fileoutpath])
      print (element+ ' done!')
      return complete
        

if __name__ == '__main__':
    pool=Pool()
    roots=pool.map(SerialBlast, (iter(L)))
    roots.start()



    
