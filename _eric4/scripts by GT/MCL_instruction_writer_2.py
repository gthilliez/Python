#script by G. Thilliez 2013
##note : Turn this script in a function with default value
#this script write a set of instruction that can be entered in the Unix command line environement Cygwin with MCL installed
#http://www.cygwin.com/
#http://micans.org/mcl/

#Import section
from datetime import datetime
import os
import re
#
#rgx=re.compile('\d{1,}') #regex use to get the index written in all the files name (see previous scripts)
CD=os.getcwd() #get the current working directory

now=datetime.now()
date=str(now.year)+'_'+str(now.month)+'_'+str(now.day)
date2=str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)
#date and date2 are use in the creation of file names below
Fo='MCLINSTRUCTION%s'%(date2) #create the file where all the instruction will be written
fileout=open(Fo, 'w') #see comment above

print>>fileout,  'cd %s'%os.getcwd().replace('\\','/')#Cygwin is a Unix environement, therefore the separator must be '/', not '\'...


BLASTfolder='BLAST/MCL_waiting_list'
BLASTFileDir=os.path.join(BLASTfolder) #Input for MCL, BLAST output in tabular format (outfmt 6);change name of folder if needed
MCLFolder='MCL_Output'
DumpFolder='dump'
OutputGraphFolder='OutputGraph'
MCLDumpDir=os.path.join(MCLFolder, DumpFolder).replace('\\','/') #output directory, must exist
OutputGraphDir=os.path.join(MCLFolder, OutputGraphFolder).replace('\\','/')

if not os.path.isdir(MCLDumpDir): #if the MCLDumpDir does not exist, create it
    os.makedirs(MCLDumpDir)



if not os.path.isdir(OutputGraphDir): #if the outputgraph dir doesn't exist, create it
    os.makedirs(OutputGraphDir)



inflationList=[3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10] #list for the inflation value to use for MCL
#manually change the member of inflationList if you want to test other inflation values

IdList=[] #if the dump file are already created, the script will ignore them and only treat the files for which no dump file were found
for files in os.listdir(MCLDumpDir):
    if files not in IdList:
        IdList.append(files)
#The for loop above check if the dump file have been created for a given index and inflation value.
#it stores the index.inflation value (x10) in a List
#eg for dump.file_0001.mci.I20 it will store Idext=0001.I20

for element in os.listdir(BLASTfolder):
    for value in inflationList:
        extention='.I'+str(int(value*10))
        MCLname=element+'_MCL_'
        outputname=element+'_MCL_'+extention
        if outputname not in IdList:
            print>>fileout,  ('cut -f 1,2,11 %s/%s >%s/%s.abc')%(
            BLASTfolder, element,MCLFolder,  MCLname) #1,2 ->prot id (query, hit) 11 ->evalue
    
            print>>fileout, ("mcxload -abc %s/%s.abc --stream-mirror "
            "--stream-neg-log10 -stream-tf 'ceil(200)' -o %s/%s.mci -write-tab "
            "%s/%s.tab" )%(MCLFolder,MCLname,MCLFolder,  MCLname,MCLFolder, MCLname)
                    
            print>>fileout, ("mcl %s/%s.mci --d -write-graphx"
            " %s/OutputGraph-%s%s -I %s")%(MCLFolder, MCLname, 
            OutputGraphDir, MCLname, extention, value) #--d write the output in the input directory
            #-I %s define an inflation , the number is defined in the inflation list #-write-graphx write the Output graph
        
            print>>fileout, ("mcxdump -icl %s/out.%s.mci%s "
            "-tabr %s/%s.tab -o %s/dump.%s.mci%s")%(
            MCLFolder, MCLname, extention,  MCLFolder,  MCLname, MCLDumpDir, 
            MCLname, extention) #create a dump file, in which all prot Id on the same line are on the same cluster
else:
    fileout.close()
