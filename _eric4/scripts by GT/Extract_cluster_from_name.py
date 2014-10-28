from sys import stdin, argv


def ExtractCluster (IdList, dumpFile, output):
    """COMMENTS"""
    fh=open(IdList)
    ListIds=[element.strip() for element in fh]
    ClusterFh=open(dumpFile)
    f_out=open(output, 'w')
    for element in ClusterFh:
        for subele in element.strip().split('\t'):
            if subele in ListIds:
                print>>f_out, '[Cluster_%s]'%(subele)
                print>>f_out, '%s'%element.strip()
    else:
        f_out.close()


ExtractCluster(argv[1], argv[2], argv[3])
