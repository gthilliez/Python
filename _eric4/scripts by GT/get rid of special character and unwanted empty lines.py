import re
AssociationHandle=open('C:\\Users\\gt41237\\associationmatrice.csv', 'rb')
NewAssociationMatrice=open('C:\\Users\\gt41237\\NewAssociationMatrice.csv', 'wb')
regex1=re.compile("\[|'|\]|\"")

for line in AssociationHandle:
    data=line.strip().split(',')
    newline='%s'%(data[1:])
    print>>NewAssociationMatrice, '%s' %(regex1.sub('',newline))
