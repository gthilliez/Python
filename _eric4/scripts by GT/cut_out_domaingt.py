from sys import stdin, argv

def CutOutDomain(coords,filename, header=False, column_id=0, column_start=8, column_stop=9):
    """COMMENTS"""
    from Bio import SeqIO
    fh=open(coords)
    seqfile=open(filename)
    Towrite=[]
    CoordIDDic={}
    if header==True:
        print 'header set to True, first line of %s will be ignored'%coords
        skip_header=fh.readline()
    else:
        print 'header not set to True, first line of %s will be processed'%coords

    for unformatedLine in fh:
        l=unformatedLine.replace('\xa0', '').strip().split(',')
        if l[column_id] not in CoordIDDic:
            CoordIDDic[l[column_id]]=l[column_start], l[column_stop]
    else:
        for s in SeqIO.parse(seqfile, 'fasta'):
            if s.id in CoordIDDic:
                start=(int(CoordIDDic.get(s.id)[0])-1)
                stop=int(CoordIDDic.get(s.id)[1])
                s.id=s.id+'_%s_%s'%((start+1), stop)
                Towrite.append(s[start:stop])
        else:
            Output=open('CutOutdomain_%s'%filename, 'w')
            SeqIO.write(Towrite, Output, 'fasta')
        





CutOutDomain(argv[1], argv[2])
