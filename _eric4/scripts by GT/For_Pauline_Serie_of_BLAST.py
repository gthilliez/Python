from Bio import SeqIO
import os

BaitDir=os.path.join(os.getcwd(), 'bait')
if not os.path.isdir(BaitDir):
    os.makedirs(BaitDir)

for rec in SeqIO.parse('bait.fasta', 'fasta'):
    BaitFasta=str(rec.id)[1::]+'.fasta'
    BaitPath=os.path.join(BaitDir, BaitFasta)
    fileout=open(BaitPath, 'w')
    SeqIO.write(rec, fileout, 'fasta')



import subprocess
import multiprocessing
from Bio.Blast.Applications import NcbiblastnCommandline
import time



##OutDir='C:\Users\gt41237\Cluster_on_RxLRs_only' #output files directory
OutDir=os.path.join(os.getcwd(), 'BLAST_output')
if not os.path.isdir(OutDir):
    os.makedirs(OutDir)

      
def SerialBlast(BaitDir,  OutDir):
  for element in os.listdir(BaitDir):
    if '.fasta' in os.path.splitext(element):
#      print element
      filepath=os.path.join(BaitDir,element)
      db_potato=os.path.join(os.getcwd(), 'potato_db')
      db_tomato=os.path.join(os.getcwd(), 'tomato_db')
      OutPutBlast_potato='Blastp%s_vs_potato.xml'%element
      fileoutpath_potato=os.path.join(OutDir,OutPutBlast_potato)
      OutPutBlast_tomato='Blastp%s_vs_tomato.xml'%element
      fileoutpath_tomato=os.path.join(OutDir,OutPutBlast_tomato)
#      print fileoutpath
      blastn=NcbiblastnCommandline(query=filepath,  db=db_potato,  evalue=1e-5, outfmt=5, out=fileoutpath_potato)
      blastn()
      blastn=NcbiblastnCommandline(query=filepath,  db=db_tomato,  evalue=1e-5, outfmt=5, out=fileoutpath_tomato)
      blastn()
#      print (element+ ' done!')
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
multiprocessing_run(SerialBlast(BaitDir, OutDir), 3, True)


    


