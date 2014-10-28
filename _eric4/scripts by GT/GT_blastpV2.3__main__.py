import subprocess
import os
#import re
import multiprocessing
from Bio.Blast.Applications import NcbiblastpCommandline
import time

#input file must be fasta format, the rgx is here to distinguish between the fasta file and the blastdb files
#rgx=re.compile('fasta$')
FileDir='C:\Users\gt41237\Cluster_on_RxLRs_only\JackKnife_dict_Pi_Pc_Ps_EER_trunc' #input files directory
OutDir='C:\Users\gt41237\Cluster_on_RxLRs_only' #output files directory

#def SerialBlast(FileDir, OutDir):
#  FDir=FileDir
#  ODir=OutDir
#  for element in os.listdir(FDir):
#    if rgx.search(element):
#      print element
#      filepath=FDir+'\\'+element
#      fileoutpath=ODir+'\\'+'SelfBLASTp'+element+'.csv'
#      testsub=subprocess.Popen(['blastp', '-query',filepath, '-db', filepath, '-evalue', '1e-5','-outfmt', '6','-out', fileoutpath])
#      print (element+ ' done!')
#      return none
      
def SerialBlast(FileDir,  OutDir):
  for element in os.listdir(FileDir):
    if '.fasta' in os.path.splitext(element):
      print element
      filepath=os.path.join(FileDir,element)
      OutPutBlast='SelfBlastp%s.csv'%element
      fileoutpath=os.path.join(OutDir,OutPutBlast)
      print fileoutpath
      blastp=NcbiblastpCommandline(query=filepath,  db=filepath,  evalue=1e-5, outfmt=6, out=fileoutpath )
      blastp()
      print (element+ ' done!')
    else:
        continue
  return 'done !'


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
                                     (str(cline), ))#,
                                     #{'stderr': subprocess.PIPE,
                                      #'shell': sys.platform != "win32"},
                                     #callback=callback_fn) \
                        for cline in clines]
    pool.close()      # Run jobs
    pool.join()
    #print_verbose_list(completed)
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
multiprocessing_run(SerialBlast(FileDir, OutDir), 3, True)


    


