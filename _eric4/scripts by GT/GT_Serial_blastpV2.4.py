#Script by G.Thilliez 2013.07.04
#The aim is to automate a serie of self blastp with a output format adapted for MCL (format tabular = format 6 NCBIblast+ standalone)
#NCBIblast+ standalone, python and biopython are recquired
#created using python 2.7, biopython 1.61 and NCBI blast 2.2.27+

#Import Section

import subprocess #needed to do the blast, cf multiprocessing run function
import os #needed in the SerialBlast function to create the blast cmd lines
import sys #needed in multiprocessing run to insure it works with different systems
import multiprocessing #needed for the multiprocessing
from Bio.Blast.Applications import NcbiblastpCommandline #to create the blast command lines
import time #evaluate the time needed for all the jobs

#input file must be fasta format, line24 (first if statement of SerialBlast) is here to distinguish between the fasta file and the blastdb files

FileDir='C:\Users\gt41237\Cluster_on_RxLRs_only\JackKnife_dict_Pi_Pc_Ps_EER_trunc' #input files directory
OutDir='C:\Users\gt41237\Cluster_on_RxLRs_only' #output files directory
#create a list of command lines that can then be used in multiprocessing run
def SerialBlast(FileDir,  OutDir):
  """create a list of command lines that can then be used in multiprocessing run"""
  L=[]
  for element in os.listdir(FileDir):
    if '.fasta' in os.path.splitext(element):
      print element
      filepath=os.path.join(FileDir,element)
      OutPutBlast='SelfBlastp%s.csv'%element
      fileoutpath=os.path.join(OutDir,OutPutBlast)
      print fileoutpath
      blastp=NcbiblastpCommandline(query=filepath,  db=filepath,  evalue=1e-5, outfmt=6, out=fileoutpath )
      L.append(blastp)
    else:
        continue
  return L #L is list of command line that will be used in the multiprocessing_run function


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
                                      callback=callback_fn) \
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
            "... multiprocessing run completed (status: %s) ..." % val ##note for later, might add an index to know which job is being runned
    else:
        print >> sys.stderr, \
            "... problem with multiprocessing run (status: %s) ..." % val
#
multiprocessing_run(SerialBlast(FileDir, OutDir), 3, True) # 3 is the number of processor used, can increase if the machine has more
##Note : Annoying thing is that on windows, cmd line keep poping up
##must find a way to keep it at the background

    


