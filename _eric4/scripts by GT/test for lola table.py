import csv
import re
#input_handle=csv.reader(open('C:\Users\gt41237\Desktop\New folder (2)\InteractionWorkfile20012013_Dundee_GT.csv', 'rb'))
file_handle=open('C:\Users\gt41237\Desktop\New folder (2)\InteractionWorkfile20012013_Dundee_GT.csv', 'rb')
regex= re.compile('[B-D]{1,2}[0-9]{1,3}_{1,2}[0-9]{5,5}')
count=1
Loladict = {}
#for row in input_handle:
for row in file_handle:
    try:
        converted_PITG_name=re.search(regex, row)
        current_name='%s'%(converted_PITG_name.group())
        if current_name==previous_name:
            count+=1
        else:
            count=1
        previous_name='%s'%(converted_PITG_name.group())
        print'%s'%(count)
        PITG_name_rank='%s_%s'%(converted_PITG_name.group(), count)
        print '%s'%(PITG_name_rank)
        Loladict[PITG_name_rank] = row.split(",")
    except:
        continue
        
##create a dictionay with the names of the interactor etc, should be usefull in the future
