

def GetCoverageId(Folder, Header=False, Print_output=True, ReturnDic=False):
    """This function calculate the % of Id and % of coverage of the query
    for each hit of a BLAST output.
    It then write it in a file (1 output per input) following this format:
    name,%id,%coverage
    need a tabular BLAST output, 25 col as defined in galaxy
    
    Arguments:
    Folder is a Folder that should contain BLAST files
    
    Header define if the input contain a header or not. default value is False
    The first line wont be skipped. If define as True, the first line will be skipped
    
    Print_output define if the output generated for each file should be printed to an output file or not
    default is set as True which means that the output files will be created. If the argument is set as anything else
    the files wont be created
    
    ReturnDic define if the generated Dic should be returned or not. Default value is False. If set as True 
    the Dic will be returned. In that case use the function as such : Var=GetCoverageId(Folder,ReturnDic=True)
    Var will be the new Dictionnary. if the function is use without associating it to a variable it will print the Dictionnary
    on screen and thus might crash your system
            The returned Dictionary contains other dictionnary.
            key= name of input file
            value=associated dictionnary #subdictionnary
                    format sub dictionnary :
                    key=(proteinA,proteinB) #tuple
                    value=[%id,%coverage] #list of floats"""
    import os
    os.chdir(Folder)
    Dic={}
    for file in os.listdir(Folder):
        try:
            print 'openning %s'%(file)
            fh=open(file)
            DicLine={}
            Dic[file]=DicLine
            if Header==True:
                SkipFirstLine=fh.readline()
            for L in fh:
                line=L.strip().split('\t')
                PercentCoverage=((float(line[7])-float(line[6])+1)*100)/float(line[22])
                if (line[0], line[1]) not in DicLine:
                    DicLine[(line[0], line[1])]=[float(line[2]),PercentCoverage ]
            print '%s done'%file
        except:
            print '%s cannot be opened or is not the right format and was therefore ignored'%file
    else:
        print 'Dictionnary created'
    if Print_output==True:
        print 'Proceding to writing output file'
        outdir='output'
        if not os.path.isdir(outdir):
            os.mkdir(outdir)
        os.chdir(os.path.join(os.getcwd(),outdir))
        for key in Dic.iterkeys():
            tempDic=Dic.get(key)
            fileout=open('percentId_and_Coverage_%s.csv'%key, 'w')
            for tempKey in tempDic.iterkeys():
                print>>fileout,  '%s,%s,%s'%('__'.join(tempKey), tempDic.get(tempKey)[0],tempDic.get(tempKey)[1] )
        else:
            fileout.close()
            print 'Done creating output files'
    if ReturnDic==True:
        return Dic


