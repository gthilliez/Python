#import csv
import re
#input_handle=csv.reader(open('C:\Users\gt41237\Desktop\New folder (2)\InteractionWorkfile20012013_Dundee_GT_2.csv', 'rb'))
file_handle=open('C:\Users\gt41237\Desktop\New folder (2)\InteractionWorkfile20012013_Dundee_GT_2.csv', 'rb')
regex_thaliana=re.compile('AT[0-9]G[0-9]{5,5}')
regex_eff_pi= re.compile('[B-D]{1,2}[0-9]{1,3}_{1,2}[0-9]{5,5}')
regex_eff_Ha=re.compile('HaRxL{1,2}[0-9]{1,3}_{0,1}[a-zA-Z]{0,5}[0-9]{0,1}')
regex_ATR=re.compile('A[R-Tr-t]{2}[0,9]{1,2}X{0,1}\.{0,1}[0,9]{0,1}[A-Ba-b]{0,1}_[A-Za-z]{0,5}[0-9]{0,1}_{0,1}[A-Z]{0,2}_{0,1}[A-Z]{0,3}\+{0,1}[A-Za-z]{0,4}')
regex_geneid=re.compile('gene_id_[0-9]{1,6}_\([A-Z]{1}[0-9]{1,2}\)')
previous_name='none'
count=1
Loladict = {}
#for row in input_handle:
for row in file_handle:
    try:
        eff_pi=re.search(regex_eff_pi, row)
        current_name='%s'%(eff_pi.group())
        print 'step 1 ok'
        if current_name==previous_name:
            count+=1
        else:
            count=1
        print 'step 2 ok'
        previous_name='%s'%(eff_pi.group())
        print'%s'%(count)
        PITG_name_rank='%s_%s'%(eff_pi.group(), count)
        PITG_key_name='%s'%(eff_pi.group())
        print '%s'%(PITG_name_rank)
        if PITG_key_name in Loladict:
            Loladict[PITG_key_name].append(row.split(","))
        else:
            Loladict[PITG_key_name] = row.split(",")
    except:
        continue
        
##create a dictionay with the names of the interactor etc, should be usefull in the future
##Test to check if everything is ok :
for row in file_handle:
    try:
        thaliana_name=re.search(regex_thaliana, row)
        thaliana_key_name='%s'%(thaliana_name.group())
        eff_pi=re.search(regex_eff_pi,  row)
        eff_pi_value='%s'%(eff_pi.group())
        if thaliana_key_name in Loladict:
            Loladict[thaliana_key_name].append(eff_pi_value)
        else:
            Loladict[thaliana_key_name] = eff_pi_value
        print '%s,%s'%(thaliana_name.group(), eff_pi_value)
    except:
        try:
            thaliana_name=re.search(regex_thaliana, row)
            thaliana_key_name='%s'%(thaliana_name.group())
            eff_Ha=re.search(regex_eff_Ha,  row)
            eff_Ha_value='%s'%(eff_Ha.group())
            if thaliana_key_name in Loladict:
                Loladict[thaliana_key_name].append(eff_Ha_value)
            else:
                Loladict[thaliana_key_name] = eff_Ha_value
            print '%s,%s'%(thaliana_name.group(), eff_Ha_value)
        except:
            try:
                thaliana_name=re.search(regex_thaliana, row)
                thaliana_key_name='%s'%(thaliana_name.group())
                ATR=re.search(regex_ATR,  row)
                ATR_value='%s'%(ATR.group())
                if thaliana_key_name in Loladict:
                    Loladict[thaliana_key_name].append(ATR_value)
                else:
                    Loladict[thaliana_key_name] = ATR_value
                print '%s,%s'%(thaliana_name.group(), ATR_value)
            except:
                try:
                    thaliana_name=re.search(regex_thaliana, row)
                    thaliana_key_name='%s'%(thaliana_name.group())
                    geneid=re.search(regex_geneid,  row)
                    geneid_value='%s'%(geneid.group())
                    if thaliana_key_name in Loladict:
                        Loladict[thaliana_key_name].append(geneid_value)
                    else:
                        Loladict[thaliana_key_name] = geneid_value
                    print '%s,%s'%(thaliana_name.group(), geneid_value)
                except:
                    continue
        
