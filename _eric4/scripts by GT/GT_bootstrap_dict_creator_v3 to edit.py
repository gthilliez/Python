import random
from Bio.SeqUtils import quick_FASTA_reader


file_handle=raw_input('Enter input filepath of the P. infestans and P. capsici trimmed sequences: ') 
entries = quick_FASTA_reader(file_handle)

seqdict={}
entries=quick_FASTA_reader(file_handle)
for name,  seq in entries:
    seqdict[name]=seq
        
bootstrapdict_1={}
while len(bootstrapdict_1)<30000:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_1[key]=value

bootstrapdict_2={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_2[key]=value

bootstrapdict_3={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_3[key]=value

bootstrapdict_4={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_4[key]=value
    
bootstrapdict_5={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_5[key]=value
    
bootstrapdict_6={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_6[key]=value
    
bootstrapdict_7={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_7[key]=value
    
bootstrapdict_8={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_8[key]=value
    
bootstrapdict_9={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_9[key]=value
    
bootstrapdict_10={}
for name,  seq in entries:
    entry=random.choice(seqdict.items())
    key='%s'%(entry[0])
    value='%s'%(entry[1])
    bootstrapdict_10[key]=value

fileout1=open('C:\Users\gt41237\Bootstrapdict1.txt', 'wb')
for key in bootstrapdict_1:
	print>>fileout1, ">%s" %(key)
	print>>fileout1, (bootstrapdict_1.get(key))
    
fileout2=open('C:\Users\gt41237\Bootstrapdict2.txt', 'wb')
for key in bootstrapdict_2:
	print>>fileout2, ">%s" %(key)
	print>>fileout2, (bootstrapdict_2.get(key))
    
fileout3=open('C:\Users\gt41237\Bootstrapdict3.txt', 'wb')
for key in bootstrapdict_3:
	print>>fileout3, ">%s" %(key)
	print>>fileout3, (bootstrapdict_3.get(key))
    
fileout4=open('C:\Users\gt41237\Bootstrapdict4.txt', 'wb')
for key in bootstrapdict_4:
	print>>fileout4, ">%s" %(key)
	print>>fileout4, (bootstrapdict_4.get(key))
    
fileout5=open('C:\Users\gt41237\Bootstrapdict5.txt', 'wb')
for key in bootstrapdict_5:
	print>>fileout5, ">%s" %(key)
	print>>fileout5, (bootstrapdict_5.get(key))
    
fileout6=open('C:\Users\gt41237\Bootstrapdict6.txt', 'wb')
for key in bootstrapdict_6:
	print>>fileout6, ">%s" %(key)
	print>>fileout6, (bootstrapdict_6.get(key))
    
fileout7=open('C:\Users\gt41237\Bootstrapdict7.txt', 'wb')
for key in bootstrapdict_7:
	print>>fileout7, ">%s" %(key)
	print>>fileout7, (bootstrapdict_7.get(key))
    
fileout8=open('C:\Users\gt41237\Bootstrapdict8.txt', 'wb')
for key in bootstrapdict_8:
	print>>fileout8, ">%s" %(key)
	print>>fileout8, (bootstrapdict_8.get(key))
    
fileout9=open('C:\Users\gt41237\Bootstrapdict9.txt', 'wb')
for key in bootstrapdict_9:
	print>>fileout9, ">%s" %(key)
	print>>fileout9, (bootstrapdict_9.get(key))
    
fileout10=open('C:\Users\gt41237\Bootstrapdict10.txt', 'wb')
for key in bootstrapdict_10:
	print>>fileout10, ">%s" %(key)
	print>>fileout10, (bootstrapdict_10.get(key))
    
fileout1.close()
fileout2.close()
fileout3.close()
fileout4.close()
fileout5.close()
fileout6.close()
fileout7.close()
fileout8.close()
fileout9.close()
fileout10.close()
