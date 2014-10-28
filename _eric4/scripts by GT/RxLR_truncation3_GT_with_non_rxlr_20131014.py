# RxLR_truncation.py
# Attempt to make a working script to truncate RxLR after EER motif, RxLR effector are defined according to the publication form whisson et al 2007 + suplementals doi: 10.1038/nature06203
# A number of elements are copied directly from a script by Leighton Pritchard
# Remco Stam 2012, edited by Gaetan Thilliez 2013
#the regex has been changed, to truncate at the first RXLR and EER encounter
# is a comment
# IMPORTS


from Bio.Alphabet import IUPAC
from Bio.Seq import Seq ##
from Bio.SeqRecord import SeqRecord ##
from Bio.SeqUtils import quick_FASTA_reader
from Bio import SeqIO

# This part is made by looking at LP's truncate_core_aa.py

import re
regex = re.compile('R.LR.{,60}?[ED][ED][KR]|R.LR.{,40}?[QD][QD]K|R.LR') #define the RxLR EER motif, looks also for alternative of the EER such as DDK, if the EER is not their, the truncation will occur after the RxLR motif
#the regex has been changed, {,60} alone would look for the longest sequence possible between RxLR and EER, whereas {,60}? will take the smallest distance between RxLR and EER, so if there is two EER motif, the first one will be used
file_handle='D:\Databases\All_RxLR_121216_aa_simpleName.fasta' #ask for the fasta file directory, the input file should be a fasta file with simple names for each sequence
entries = quick_FASTA_reader(file_handle) #open the fasta file
oname= 'D:\Databases\All_RxLR_121216_aa_simpleName_EER_trunc20131014.fasta' #ask for the output file directory, the file will be created by the script
reportfilepath='D:\Databases\Report_EER_trunc20131014.fasta'#create a file containing all the sequence that do not have a RxLR motif as defined by the regex
reportfile=open(reportfilepath, 'w')
print>>reportfile, 'This file contain the sequences that do not have a predicted RxLR motif'

# make a dictionary with the positions where to split the sequences
splitdict = {}
for name, seq in entries:
    try:
        match = re.search(regex, seq) #search for the RxLR EER motif
        motif = match.group() #print the seq from the start codon to the EER 
        span = match.span() #print the position of the RxLR EER motif
        print("Name: %s, Size: %s, Motif: %s, End: %s"%(name,len(seq), motif, span)) # some things to see if everything is working fine
        splitdict[name] = span[1] #add the position of the end of the RxLR EER motif in the dictionary
    except: #this line is their to avoid crash when the program encounter a non RxLR effector (effector that does not match with the definition given in Whisson et al 2007)
        print('%s, does not have a RxLR motif')%(name) #give the name of the non RxLR in the input file
        print>>reportfile, '>%s'%name
        print>>reportfile,  '%s'%seq
        continue #if continue is not there, the for loop would start from the beginning again


# the next bit is adapted from better_shorter_script.py from LP

# Load FASTA sequences and split on the cleavage site

truncated = [] 
for s in SeqIO.parse(file_handle, 'fasta'):
    try:
        truncated.append(s[splitdict[s.id]:])
    except:
        continue 

#the seqio parser will read the input file and for each sequence it will try to truncate them after the EER domain thanks to the data in the splitdict. If their is a non RxLR, the data won't be available in the splitdict. In this case the expcept loop will be apply
SeqIO.write(truncated, oname, 'fasta')  #write the truncated sequence in a fasta file
reportfile.close()


