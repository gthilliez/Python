from Bio.SeqUtils import quick_FASTA_reader
import re
regex_PITG= re.compile('PITG_[0-9]{4,6}')
PiAllProtFilePath='D:\Databases\Genomes sequences\phytophthora_infestans_t30-4_1_proteins.fasta' #File containing all predicted protein from P. infestans (fasta format)
Pientries = quick_FASTA_reader(PiAllProtFilePath) #open the file using the FASTA reader module
PiOutFilePath='D:\Cluster201308\TrimmedPiProt20131014.fasta' #Output file
PiOutFile=open(PiOutFilePath, 'w') #open the output file in writing mode
PITGdict = {} #create a dictionary, key will be name of protein and entry will be sequence

for name, seq in Pientries: # file dictionnary with name and sequences info from the P. infestans predicted protein set
        match=re.search(regex_PITG, name)
        PITGName=match.group()
        PITGdict[PITGName] = seq


PiTruncRxLRFilePath='D:\Databases\All_RxLR_121216_aa_simpleName_EER_trunc20131014.fasta' #path to the truncated RxLR dataset
PiRxLRentries=quick_FASTA_reader(PiTruncRxLRFilePath)
OverWrite=[] #create a list that will contain info about the RXLR sequences replaced by truncated RXLR
NewlyAdded=[]

for name, seq in PiRxLRentries:
    if 'PITG' in name.split('_'):
        match=re.search(regex_PITG, name)
        PITGName=match.group()
        if PITGName in PITGdict:
            OverWrite.append((PITGName, seq, PITGdict.get(PITGName))) #overwrite list will contain name of the sequence replace. the truncated sequence and the full sequence
        else:
            NewlyAdded.append((PITGName, seq))
        PITGdict[PITGName] = seq #overwrite the sequence

print '%s full length predicted RXLR sequences have been replaced by truncated sequences'%len(OverWrite)
print'%s truncated sequences have been newly added to the P. infestans predicted protein set'%len(NewlyAdded)

for key in PITGdict.iterkeys():
    print>>PiOutFile,  '>%s'%key
    print>>PiOutFile,  '%s'%PITGdict.get(key)


    
PiOutFile.close()
    
