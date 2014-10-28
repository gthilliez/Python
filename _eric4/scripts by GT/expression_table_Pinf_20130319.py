PITG_expression={}
Import_expression_table1=raw_input('path to the expression table: ')
Import_expression_table2=raw_input('path to the expression table: ')
File_handle1=open(Import_expression_table1, 'rb')
File_handle2=open(Import_expression_table2, 'rb')

for line in File_handle1:
    data=line.split(',')
    PITG_expression[data[0]]=data[1], data[2], data[3]
        
for line in File_handle2:
    data=line.split(',')
    if data[0] in PITG_expression:
        PITG_expression[data[0]]=PITG_expression.get(data[0]), data[4]
    else:
        PITG_expression[data[0]]=data[1], data[2], data[3], data[4]
        
fileout=open('C:\Users\gt41237\expression_tablePi.csv', 'wb')
print>>fileout,  'ID,Expression_Blue13,Expression_T30-4,Expression_NL07434,Expression_88069'
for key in PITG_expression:
	print>>fileout, '%s_1,%s' %(key,PITG_expression.get(key))
