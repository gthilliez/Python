import subprocess
import os
import re

rgx=re.compile('fasta$')
FileDir='C:\Users\gt41237\Cluster_on_RxLRs_only\JackKnife_dict_Pi_Pc_Ps_EER_trunc'
for element in os.listdir(FileDir):
    if rgx.search(element):
        filepath=FileDir+'\\'+element
        testsub1=subprocess.Popen(['makeBlastdb', '-in',filepath, '-dbtype', 'prot', '-out', filepath])
