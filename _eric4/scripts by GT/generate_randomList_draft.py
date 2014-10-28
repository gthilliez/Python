from sys import stdin, argv
import time
import csv
import os
import random

def GenerateRandomList(InputList, leave_out_percentage, num_sets):
    """InputList is a List file, should work with one value per line
    Leave_out_percentage is a value between 0 and 1 that represent the % of seq to leave out; eg, 0.2 to leave 20% of the sequence out
    num_sets is a intergrer that correspond to the number of sets to generate
    BLAST is a BLAST output to use as a basis for the JackKnifing. 
    evalue is an evalue cutoff; eg, 0.1 ; 1e-5 etc...
    col_evalue is the number of the column in which the evalue is stored. for a standard tabular BLAST output, it is column 11"""

    InputFile=open(InputList)
    seqlist = [l.strip() for l in InputFile.readlines()] #list of protein id
    
    t0 = time.time()
    
    print "Read %d sequences names into memory in %.2fs" % (len(seqlist), time.time() - t0) 
    seq_count=int(len(seqlist)*(1-float(leave_out_percentage)))
    ##--Create a Dictionnary that contain "num_sets" entries
    ##each key is a number, each value is a list of protein id--#
    JackKnifeDic={}
    for i in range(int(num_sets)):
        random.shuffle(seqlist)
        JackKnifeDic[i]=seqlist[:seq_count]
            
    print "Generated set of %d jackknife in %.2fs" %\
    (len(JackKnifeDic), time.time()-t0)
    
    ##-- Create JK output--#
    for Key in JackKnifeDic:
        OutputFile=open('Dataset_%s.fasta'%Key, 'w')
        for value in JackKnifeDic.get(Key):
            print>>OutputFile, value
        else:
            OutputFile.close()


GenerateRandomList(argv[1], argv[2], argv[3])
