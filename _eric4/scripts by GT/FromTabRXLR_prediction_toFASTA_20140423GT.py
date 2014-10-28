#Script by Gaetan Thilliez 2014-04-23
#The aim of the script is to read tabular output files from galaxy (for the prediction of RXLRs)
#and create a fasta file containing all the positive results
#can be used for several tab file at the same time, no redundancy created



def FastaFromPredictionRXLR (Fasta,output, idcolumn=0, SelectionColumn=1,SelectionList=['Y', 're', 'hmm'],  Header=True, sep='\t', *args, **kwargs ):
    """Comments
    This function aim to use one or more RXLR prediction tabular file and create a matching fasta file
    This function will not create redundancy. If a protein id is present in several prediction file used at the same time, 
        the sequence will be present only once in the final fasta. 
    This function do not look for physical overlap.
    
    Fasta : type == str( path to the fasta file used to predict RXLRs 
    output: type == str; path used to generate the output fasta file
    idcolumn: type==int; Python index corresponding to the column containing the id of the protein
        eg in the standard output of the Galaxy RXLR prediction tool, the first column contain the name; therefore the corresponding python index is 0 (default value)
    SelectionColumn : type==int; Python index corresponding to the column containing the selection value
        eg in the standard output of the Galaxy RXLR prediction tool, it's the 2nd column, so python index is 1 (default)
    SelectionList : type== list of str; Acceptable values found in the SelectionColumn to be added to the list of protein to add to the final fasta
        By default the values are 'Y','re','hmm' which correpond to the notation system used by the Whisson et al 2007 model
        
        Y = Yes, both the heuristic motif and HMM were found.
        re = Only the heuristic SignalP with regular expression motif was found.
        hmm = Only the HMM was found.
        neither = Niether the heuristic motif nor HMM was found.

        The Bhattacharjee et al. (2006) RXLR Model and Win et al. (2007) RXLR Model uses
        Y= is predicted to be RXLR by the model
        N= is NOT predicted to be RXLR by the model
        
    Header : type==any; If True, skip the first line, else keep the first line
        default output from galaxy, Header=True
    sep : type == str, define the separator between the different column; default separator for RXLR prediction tool in Galaxy is tab so sep='\t'
    *args= not in use
    *kwargs : type == key word defined str; they are a list of the tabular file you want to use.
        eg to use only one tabular file called "Win2007.tabular" add the argument at the end of the function with a variable name
        FastaFromTabularRXLR('Fasta.fasta','Output.fasta',Win='Win2007.tabular')
        the variable name Win could be anything you want
        to use several predictions output : if 2nd prediction is called 'whisson2007.tabular'
        FastaFromTabularRXLR('Fasta.fasta','Output.fasta',Win='Win2007.tabular',Whisson2007='whisson2007.tabular')
        
        use as many key word arguments as you like
        This function will not create redundancy. If a protein id is present in several prediction file used at the same time, 
        the sequence will be present only once in the final fasta. 
        This function do not look for physical overlap.
    """
    print "tabular files used :%s"%kwargs
    from Bio import SeqIO
    FhFasta=open(Fasta)
    FastaDic={Seq.id:Seq
        for Seq in SeqIO.parse(FhFasta, 'fasta')}
        
    Dic={}
    for k,  value in kwargs.iteritems():
        fh=open(value)
        if Header==True:
            fh.readline()
        for UnformatedLine in fh:
            line=UnformatedLine.strip().split(sep)
            if line[SelectionColumn] in SelectionList:
                Dic[line[idcolumn]]=FastaDic.get(line[idcolumn])
    else:
        print 'ok so far'
        Out=open(output, 'w')
        print 'writting %s sequences'%len(Dic.values())
        SeqIO.write(Dic.values(), Out, 'fasta')
        Out.close()
        print 'done'


#import os
#os.chdir('D:\Databases\Genomes_sequences\Pparasitica\INRA310\RXLR-prediction')
#FastaFromPredictionRXLR('Galaxy3-[CDSs_(amino_acids)].fasta','PredictedRXLR.fasta',win='Galaxy5-[Win_et_al._(2007)_RXLR].tabular', whisson='Galaxy7-[Whisson_et_al._(2007)_RXLR-EER_with_HMM].tabular' )
