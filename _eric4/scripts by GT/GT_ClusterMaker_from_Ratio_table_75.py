RatioTableHandle=open('C:\\Users\\gt41237\\ratiomatriceRXLRNEW.csv', 'rb')
Assoc75={}
ColDict={}
count=0
for line in RatioTableHandle:
    data=line.strip().split(',')
    count=count+1 #get rid of first line
    if count ==1:
        countcol=-3
        for entry in data:
            countcol=countcol+1
            if countcol>-1:
                ColDict[countcol]=data[countcol]
    if count>1:
        count2=-3
        for entry in data:
            count2=count2+1 #get rid of first 2 column on every line
            if count2>-1 and float(entry)>0.75:
                if data[1] in Assoc75:
                    Assoc75[data[1]]=Assoc75[data[1]], ColDict[count2], data[count2]
                else:
                    Assoc75[data[1]]=(ColDict[count2], data[count2])    ##Problen with the count2. it is shifted 2 col on the left (to obtain the real association, use count2+2 an indicator. But why?)
                
                
    
    #data[1]=effecto ID
