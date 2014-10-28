from Bio import SeqIO

db='C:\Users\gt41237\Clustering_GT_2013\Databases\Updated_trimmed_PITG_and_PcRxLR_20130214.txt'
seqdict={}

for rec in SeqIO.parse(db, 'fasta'): ##
    seqdict[rec.id]=rec
    if rec.id == 'PITG_21238': #change to the name of the sequence to extract
        print rec
        
#alternativly
seqdict.get('PITG_21238') #change to the name of the sequence to extract
