AssociationHandle=open('C:\\Users\\gt41237\\NewAssociationMatrice.csv', 'rb')
import re
regex1=re.compile('\d{1,2}')
regex2=re.compile("\[|'|\]|\"")
#Switch=1
x=1
#ColDict={}
#while Switch!=0:
#    for line in AssociationHandle:
#        data=line.strip().split(',')
#        for value in data:
#            print x
#            if x !=38125:
#                ColDict[x]=data[x]
#                x=x+1
#        Switch=0
        
for line in AssociationHandle:
    data=line.strip().split(',')
    if x==1:
        break
fileout=open('C:\\Users\\gt41237\\RatioMatriceTest.csv', 'wb')
print>>fileout, '%s' %(line)


PresenceHandle=open('C:\\Users\\gt41237\\presencematrice.csv', 'rb')
#x=1
PresenceDict={}
for line in PresenceHandle:
    data=line.strip().split(',')
    PresenceDict[x]=data[1]
    x=x+1

d=0
MatriceDict={}
for line in AssociationHandle:
    d=d+1
    print 'line %s' %(d)
    y=0
    data=line.strip().split(',')
    for value in data:
        strdata='%s'%(data[y].strip())
        mo=re.match(regex1, strdata)
        if y!=0 and mo!= None and mo.group()=='%s'%(data[y].strip()) and data[y]!=0 : 
            key='NoOneCares'
            MatriceDict[key]=[0]*38124
            MatriceDict[key][y-1]=(float(data[y])/float(PresenceDict.get(y)))
#        else:
#            continue
        y=y+1
    print>>fileout,  '%s, %s'%(d-1, regex2.sub('', str(MatriceDict.get(key))))
            
