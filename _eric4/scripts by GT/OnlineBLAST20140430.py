

def OnlineBLAST(FastaFile, OutputFile, BLAST_Type='blastn', db='nr'):
    """ FastaFile is a  user defined path leading to the fasta file used as a query
        Output file is a user defined path that will be used to create an output file. The file is 
            created by the script and if the file already exist it will be replaced.
            the output format is XML
        BLAST_Type is the program to use it can be blastn, blastp, blastx, tblastn, or tblastx (lower case)
            (see documentation of Bio.Blast.NCBIWWW)
        db is the NCBI database that should be used for the search. by default it's nr
        
        Function created based on the bio python cook book http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec95 """
    from Bio.Blast import NCBIWWW
    from Bio import SeqIO
    Fh=open(FastaFile)
    save_file = open(OutputFile, "w")
    records=[seq for seq in SeqIO.parse(Fh, 'fasta')]
    for record in records:
        result_handle = NCBIWWW.qblast(BLAST_Type, db, record.format('fasta'))
        save_file.write(result_handle.read())
    else:
        save_file.close()
        result_handle.close()
