from sys import stdin, argv #to run script on cmd line

def KVXF_finder2 (fasta): 
    """Needs a fasta input; will create a fasta output if the motif is found
    The script looks for the KVXF aka RVXF motif derived Templeton et al 2012 :[HKR][ACHKMNQRSTV]{0,1}V[CHKNQRST][FW]
    This script requires python v 2.7 and biopython
    
    ref Templeton et al 2012 Identification and characterization of AtI-2, an Arabidopsis homologue of an
ancient protein phosphatase 1 (PP1) regulatory subunit
Gaetan Thilliez 07.07.2014"""
    from Bio import SeqIO
    import re
    KVXF=re.compile('[HKR][ACHKMNQRSTV]{0,1}V[CHKNQRST][FW]') #motif 
    ToWrite=[]

    for seq in SeqIO.parse(fasta, 'fasta'): #parse the fasta file and look at each sequence individually
        if re.search(KVXF,  str(seq.seq.upper())): #if the motif in the seq
            Matches=re.finditer(KVXF,  str(seq.seq.upper())) #find all the occurance of the motif
            for Motif in Matches:
                seq.description=seq.description + '|%s %s %s'%(Motif.group(),Motif.span()[0],Motif.span()[1]) #modify the description to give info on the motif (motif and position)
            else:
                ToWrite.append(seq) #add the sequence to the list of sequence to write

    if len(ToWrite)>0: #if at least one sequence was found with the motif
        output=open('%s_KVFX_extended.fasta'%(fasta), 'w') #create output file
        SeqIO.write(ToWrite, output, 'fasta') #write sequence in ouput file with fasta format
        output.close() #close output file
    else:
        print 'no KVXF motif found in the provided fasta file : %s'%fasta #if no sequence have the motif then print this statement



KVXF_finder2(argv[1]) #used to run the script from command line, in windows. just type the name of the script and the input file and it will run on its own

