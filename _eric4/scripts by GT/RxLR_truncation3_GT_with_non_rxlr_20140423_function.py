# RxLR_truncation.py
# Attempt to make a working script to truncate RxLR after EER motif, RxLR effector are defined according to the publication form whisson et al 2007 + suplementals doi: 10.1038/nature06203
# A number of elements are copied directly from a script by Leighton Pritchard
# Remco Stam 2012, edited by Gaetan Thilliez 2013-2014

#the regex has been changed, to truncate at the first RXLR and EER encounter
# is a comment
# IMPORTS

def TruncationRXLRGT_RS(Input, Output, *args, **kwargs):
    """Comments
    Input is the name of input fasta file containing RXLR seq
    Output is the name to be use as an output file
    the script will truncate RXLR-EER after the EER seq if found, else after the RXLR seq
    if there is no strict RXLR motif, the sequence will just be ignored"""
    import re
    from Bio.SeqUtils import quick_FASTA_reader
    from Bio import SeqIO
    regex = re.compile('R.LR.{,60}?[ED][ED][KR]|R.LR.{,40}?[QD][QD]K|R.LR') #define the RxLR EER motif, looks also for alternative of the EER such as DDK, if the EER is not their, the truncation will occur after the RxLR motif
    #the regex has been changed, {,60} alone would look for the longest sequence possible between RxLR and EER, whereas {,60}? will take the smallest distance between RxLR and EER, so if there is two EER motif, the first one will be used
     #ask for the fasta file directory, the input file should be a fasta file with simple names for each sequence
    entries = quick_FASTA_reader(Input) #open the fasta file
    splitdict = {}
    for name, seq in entries:
        try:
            match = re.search(regex, seq) #search for the RxLR EER motif
            motif = match.group() #print the seq from the start codon to the EER 
            span = match.span() #print the position of the RxLR EER motif
            print("Name: %s, Size: %s, Motif: %s, End: %s"%(name,len(seq), motif, span)) # some things to see if everything is working fine
            splitdict[name] = span[1] #add the position of the end of the RxLR EER motif in the dictionary
        except: #this line is their to avoid crash when the program encounter a non RxLR effector (effector that does not match with the definition given in Whisson et al 2007)
            continue #if continue is not there, the for loop would start from the beginning again
    truncated = []
    file_handle=open(Input)
    for s in SeqIO.parse(file_handle, 'fasta'):
        print 'ok HERE'
        try:
            print 'ok 2'
            truncated.append(s[splitdict.get(s.id):])
            print len(truncated)
        except:
            continue 

#the seqio parser will read the input file and for each sequence it will try to truncate them after the EER domain thanks to the data in the splitdict. If their is a non RxLR, the data won't be available in the splitdict. In this case the expcept loop will be apply
    OutputFile=open(Output, 'w')
    SeqIO.write(truncated, OutputFile, 'fasta')  #write the truncated sequence in a fasta file
    OutputFile.close()
    print "%s RXLR truncated"%(len(truncated))


