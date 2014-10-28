import random
from Bio.SeqUtils import quick_FASTA_reader
print 'JackKnife_Dictionnary_maker by Gaetan Thilliez'
print 'This script is used to randomly select a subset of data from a dataset'
print 'The size of the subset and the number of subsets created are defined by the user'

file_handle=raw_input('Enter input filepath of the sequence file to use: ') 
entries = quick_FASTA_reader(file_handle)


seqdict={}

for name,  seq in entries:
    seqdict[name]=seq

print '%s sequences in the loaded file' %(len(seqdict))
Question_1=raw_input('What is the size of the JackKnifed files you want to create? : ')
Question_2=raw_input('How many JackKnifed file do you want to create? : ')




MyList=list(xrange(int(Question_2)))
for element in MyList:
    bootstrapdict={}
    while len(bootstrapdict)<int(Question_1):
        entry=random.choice(seqdict.items())
        key='%s'%(entry[0])
        value='%s'%(entry[1])
        bootstrapdict[key]=value
        pathout='C:\Users\gt41237\JackKnifeDictRxLR_%s' %(element+1)
        fileout=open(pathout, 'wb')
    for key in bootstrapdict:
        print>>fileout, ">%s" %(key)
        print>>fileout, (bootstrapdict.get(key))
    fileout.close()
