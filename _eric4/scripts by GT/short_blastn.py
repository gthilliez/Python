from Bio import SeqIO
import os
from sys import stdin,argv
import subprocess
import multiprocessing
from Bio.Blast.Applications import NcbiblastnCommandline
import time


def BLASTn_Short(Query, BLASTdb, Evalue, outfmt=6):
    """Comments"""
    if os.path.isdir(Query):
        for file in os.listdir(Query):
            Outputfile='BLASTn_%s_vs_%s_evalue_%s_%s_%s'%(file, BLASTdb, time.localtime()[0], time.localtime()[2], time.localtime()[2])
            blastn=NcbiblastnCommandline(query=os.path.join(Query, file),  db=BLASTdb,  evalue=Evalue, outfmt=outfmt, out=Outputfile, task='blastn-short')
            blastn()
        else:
            return blastn
    else:
        Outputfile='BLASTn_%s_vs_%s_evalue_%s_%s_%s'%(file, BLASTdb, time.localtime()[0], time.localtime()[2], time.localtime()[2])
        blastn=NcbiblastnCommandline(query=Query,  db=BLASTdb,  evalue=Evalue, outfmt=outfmt, out=Outputfile, task='blastn-short')
        blastn()
        return blastn


#This part is adapted from Leighton's script 
def multiprocessing_run(clines, poolsize, verbose):
    if verbose:
        t0 = time.time()
        print "Running %d jobs with multiprocessing ..." % \
            len(clines)
    pool = multiprocessing.Pool(processes=poolsize)      # create process pool
    completed = []
    if verbose:
        callback_fn = multiprocessing_callback
    else:
        callback_fn = completed.append
    pool_outputs = [pool.apply_async(subprocess.call,
                                     (str(cline), ),
                                     {'stderr': subprocess.PIPE,
                                      'shell': sys.platform != "win32"},
                                     callback=callback_fn) 
                        for cline in clines]
    pool.close()      # Run jobs
    pool.join()
    print_verbose_list(completed)
    print ("... all multiprocessing jobs ended (%.3fs)" % (time.time() - t0))

def multiprocessing_callback(val):
    """ A verbose callback function for multiprocessing runs.  It uses the
        return value to indicate run completion or failure.  Failure is
        indicated by a nonzero return from the multiprocessing call.
    """
    if 0 == val:
        print >> sys.stderr, \
            "... multiprocessing run completed (status: %s) ..." % val
    else:
        print >> sys.stderr, \
            "... problem with multiprocessing run (status: %s) ..." % val
#
BLASTn_Short(argv[1], argv[2], argv[3])
