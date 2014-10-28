iname= raw_input('Enter path to the file you want to modify: ')
filehandle=open(iname,'r')

oname= raw_input('Enter output filename: ')
fileout=open(oname, 'w')

TheDictionnary={}
for row in filehandle:
    data=row.split()
    TheDictionnary[data[0]]=data[1]
    TheDictionnary[data[0]].append(data[2])
    TheDictionnary[data[0]].append(data[3])
    TheDictionnary[data[0]].append(data[4])
    TheDictionnary[data[0]].append(data[5])

for key in TheDictionnary:
    try:
        print>>fileout, "%s %s" %(key, TheDictionnary[key][0])
        try:
            print>>fileout, "%s %s" %(key, TheDictionnary[key][1])
            try:
                print>>fileout, "%s %s" %(key, TheDictionnary[key][2])
                try:
                    print>>fileout, "%s %s" %(key, TheDictionnary[key][3])
                    try:
                        print>>fileout, "%s %s" %(key, TheDictionnary[key][4])
                    except:
                        continue
                except:
                    continue
            except:
                continue
        except:
            continue
    except:
        continue
        
fileout.close()
