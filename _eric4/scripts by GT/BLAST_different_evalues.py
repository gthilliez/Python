from Bio import SeqIO
import os

import subprocess
import multiprocessing
from Bio.Blast.Applications import NcbiblastnCommandline
import time


def BLASTDif_evalues(Query, BLASTdb, ListEvalues, BLASTType, outfmt=6):
    """Comments"""
    if BLASTType=='n':
        from Bio.Blast.Applications import NcbiblastnCommandline
        for Evalue in ListEvalues:
            Outputfile='BLASTn_%_vs_%s_evalue_%s'
            blastn=NcbiblastnCommandline(query=Query,  db=BLASTdb,  evalue=Evalue, outfmt=outfmt, out=Outputfile)
            blastn()
        else:
            return blastn
            
            
    elif BLASTType=='p':
        for Evalue in ListEvalues:
            Outputfile='BLASTn_%_vs_%s_evalue_%s'
            blastp=NcbiblastpCommandline(query=Query,  db=BLASTdb,  evalue=Evalue, outfmt=outfmt, out=Outputfile)
            blastp()
        else:
            return blastp()




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
#multiprocessing_run(BLASTDif_evalues(Query, BLASTdb, ListEvalues, BType), 3, True)
#
#Query='RXLRExtended_20140408.fasta'
#BLASTdb='RXLRExtended_20140408.fasta'
#ListEvalues=['1e%d'%i for i in range(5, 81)] 
#BType='p'
    


