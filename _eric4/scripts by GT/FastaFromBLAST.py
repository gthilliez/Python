

def FastaFromBLAST(BLAST, RefFASTA, sep='\t'):
    """Comments"""
    from Bio import SeqIO
    BLASTHandle=open(BLAST)
    IdList=[]
    for UnformatedLine in BLASTHandle:
        line=UnformatedLine.strip().split(sep)
        Query=line[0]
        Hit=line[0]
        if Query not in IdList:
            IdList.append(Query)
        if Hit not in IdList:
            IdList.append(Hit)
    else:
        FilteredFasta=[]
        Fh_FASTA=open(RefFASTA)
        for seq in SeqIO.parse(Fh_FASTA, 'fasta'):
            if seq.name in IdList:
                FilteredFasta.append(seq)
        else:
            return FilteredFasta



#BLASTFile='D:\Clustering20131212\Try_Extended_RXLR_BLAST\BLASTOutput_RXLRExtended_20140408.csv'
#RefFASTA='D:\Clustering20131212\Combined_TrimmedPi_and_Pc_20131212.fasta'
#ToWrite=FastaFromBLAST(BLASTFile, RefFASTA, ',')
#OutputFile=open('D:\Clustering20131212\Try_Extended_RXLR_BLAST\RXLRExtended_20140408.fasta', 'w')
#from Bio import SeqIO
#SeqIO.write(ToWrite, OutputFile, 'fasta')
#OutputFile.close()
