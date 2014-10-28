import re
from Bio.SeqUtils import quick_FASTA_reader
regex_PITG= re.compile('PITG_[0-9]{5,6}')
file_handle=raw_input('Enter input filepath of the P. infestans predicted protein sequences: ') 
entries = quick_FASTA_reader(file_handle)
oname= raw_input('Enter output filename: ')
fileout=open(oname, 'w')
PITGdict = {}
for name, seq in entries:
    try:
        temp_PITG= re.search(regex_PITG, name) #search for the PITG_xxxxxx name where x is a number
        PITG_name = temp_PITG.group() 
        print("%s"%(PITG_name)) # to see if everything is working fine
        PITGdict[PITG_name] = seq
    except: #this line is their to avoid crash when the program encounter a non RxLR effector (effector that does not match with the definition given in Whisson et al 2007)
        print('%s, does not have a PITG standard name')%(name) #give the name of the non RxLR in the input file
        continue #if continue is not there, the for loop would start from the beginning again

file_handle_2=raw_input('Enter input filepath of the P. infestans truncated RxLR: ')
entries_2=quick_FASTA_reader(file_handle_2)
for name, seq in entries_2:
    try:
        temp_PITG_trunc=re.search(regex_PITG, name)
        PITG_name=temp_PITG_trunc.group()
        print("%s"%(PITG_name)) # to see if everything is working fine
        PITGdict[PITG_name] = seq
    except: #this line is their to avoid crash when the program encounter a non RxLR effector (effector that does not match with the definition given in Whisson et al 2007)
        print('%s, does not have a PITG standard name')%(name) #give the name of the non RxLR in the input file
        continue #if continue is not there, the for loop would start from the beginning again

for name, seq in entries_2:
    try:
        temp_PITG_trunc=re.search(regex_PITG,  name)
        PITG_name=temp_PITG_trunc.group()
        print("%s"%(PITG_name))
        PITG_name in PITGdict
    except: #this line is their to avoid crash when the program encounter a non RxLR effector (effector that does not match with the definition given in Whisson et al 2007)
        print('%s, does not have a PITG standard name')%(name) #give the name of the non RxLR in the input file
        continue #if continue is not there, the for loop would start from the beginning again
for key in PITGdict:
	print>>fileout, ">%s" %(key)
	print>>fileout, (PITGdict.get(key))
#this 3 previous line re-create a fasta file containing the name of the predicted protein and corresponding sequence. In the case of the RxLR the Full length seq have been over-written by the lines 21-29
fileout.close()
