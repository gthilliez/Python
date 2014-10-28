import os
import shutil
DoneList=[]

for file in os.listdir('MCL_Output\dump'):
	if 'JK' in file.replace('.','_').split('_'):
		index = file.split('_')[3:5]
		DoneList.append(index)

print '%s file done so far'%len(DoneList)
MovedList=[]
waitingFolder='BLAST\MCL_waiting_list'
DoneFolder='BLAST\MCL_Done'
for file in os.listdir(DoneFolder):
	if file.split('_')[3:5] not in DoneList:
                MovedList.append(file)
                shutil.copy(os.path.join(DoneFolder,file),
                            os.path.join(waitingFolder,file))

print "%s file moved in the %s folder"%(len(MovedList),waitingFolder)

