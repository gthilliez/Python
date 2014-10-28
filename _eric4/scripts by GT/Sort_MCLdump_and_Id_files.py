import os
import shutil

cd=os.getcwd()
dic={}
MCL_Dir='JK_DUMP'
for file in os.listdir(os.join(cd, MCL_Dir)):
    if MCLExtention in file.split('.'):
        TreatedFile.append(file.split('_')[3:5])
        dic[file.split('_')[3:5]]=file
            


IDFOLDER='LISTIDJK'
Id_LIST_TO_MOVE=[]
for DB_Id_List_File in os.listdir(os.path.join(cd, IDFOLDER)):
    if DB_Id_List_File.split('_')[1:3] in TreatedFile:
        Id_LIST_TO_MOVE.append(file)
    else:
        dic.pop(DB_Id_List_File.split('_')[1:3])


DUMPTOMOVE=[]
for k in dic.iterkeys:
    DUMPTOMOVE.append(dic.get(k))

IDFOLDER2='LISTIDJK_updated'
for Id_List in Id_LIST_TO_MOVE:
    shutil.copy(os.path.join(IDFOLDER,Id_List),
                            os.path.join(IDFOLDER2,Id_List))


MCL_Dir2='JK_DUMP_updated'
for DumpFile in DUMPTOMOVE:
    shutil.copy(os.path.join(MCL_Dir2,DumpFile),
                            os.path.join(MCL_Dir2,DumpFile))
