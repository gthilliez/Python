#This script as been created to extract the P.infestans and P,capsici sequences from a RxLR database
#The script will only work if P.infestans names have a PITG_....._1 name and for P.capsici : PcRxLR..._1
#the sequence extracted will be saved in two separate files, one for infestans, the other for capsici
#Gaetan Thilliez 2013
# IMPORTS
from Bio.SeqUtils import quick_FASTA_reader
from Bio import SeqIO
import re

file_handle=raw_input('Enter input filepath: ') #ask for the fasta file directory
entries = quick_FASTA_reader(file_handle) #open the fasta file
onamePc= raw_input('Enter output filename for the P.capsici sequences: ') #ask for the output directory for the P.capsici sequences, the script will create the file
ofoutPc=open(onamePc,'w') #create and open the P.capsici output file
onamePi= raw_input('Enter output filename for the P.infestans sequences: ') #ask for the output directory for the P.infestans sequences, the script will create the file
ofoutPi=open(onamePi,'w') #create and open the P.infestans output file

for name, seq in entries:
    try:
        Pcname=re.search('PcRxLR..._1',name)
        newname = Pcname.group()
        print>>ofoutPc, ">%s" %(newname)
        print>>ofoutPc, "%s" %(seq)
    except:
        try:
            Piname=re.search('PITG_....._1',name)
            newname2 = Piname.group()
            print>>ofoutPi, ">%s" %(newname2)
            print>>ofoutPi, "%s" %(seq)
        except:
            continue
#this loop looks for patterns in the name to differenciate effector from P.capsici and P.infestans, 
#line 15 to 19, looks for P.capsici effector and print them in the P.capsici output file
#line 22 to 25 idem as above but for P.infestans
#line 26 and 27, if another kind of effector is present, it will be ignore
#in this version the script can look for PcRxLR, PITG, names which are respectively associated with Pythophthora capsici, infestans
