file_handle=open('C:\users\gt41237\desktop\dist_test2.txt','rb')
import re
default=0, 0
thedict={}
thedict['I12']=default, default, default, default, default, default, default, default
thedict['I14']=default, default, default, default, default, default, default, default
thedict['I18']=default, default, default, default, default, default, default, default
thedict['I20']=default, default, default, default, default, default, default, default
thedict['I30']=default, default, default, default, default, default, default, default
thedict['I40']=default, default, default, default, default, default, default, default
thedict['I50']=default, default, default, default, default, default, default, default
thedict['I60']=default, default, default, default, default, default, default, default
for row in file_handle:
    data=row.split()
    first_infl='%s'%(data[7])
    second_infl='%s'%(data[8])
    if first_infl=='n1=out.seq.mci.I12' and second_infl=='n1=out.seq.mci.I14':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I12'][1]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I12' and second_infl='n1=out.seq.mci.I18':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I12'][2]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I12' and second_infl='n1=out.seq.mci.I20':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I12'][3]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I12' and second_infl='n1=out.seq.mci.I30':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I12'][4]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I12' and second_infl='n1=out.seq.mci.I40':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I12'][5]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I12' and second_infl='n1=out.seq.mci.I50':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I12'][6]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I12' and second_infl='n1=out.seq.mci.I60':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I12'][7]=v1v2
        except:
            continue
#----------------------------------------------------------------------------------------------------------------------------------------
    if first_infl='n1=out.seq.mci.I14' and second_infl='n1=out.seq.mci.I18':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I14'][2]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I14' and second_infl='n1=out.seq.mci.I20':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I14'][3]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I14' and second_infl='n1=out.seq.mci.I30':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I14'][4]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I14' and second_infl='n1=out.seq.mci.I40':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I14'][5]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I14' and second_infl='n1=out.seq.mci.I50':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I14'][6]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I14' and second_infl='n1=out.seq.mci.I60':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I14'][7]=v1v2
        except:
            continue
#----------------------------------------------------------------------------------
    if first_infl='n1=out.seq.mci.I18' and second_infl='n1=out.seq.mci.I20':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I20'][3]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I18' and second_infl='n1=out.seq.mci.I30':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I20'][4]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I18' and second_infl='n1=out.seq.mci.I40':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I20'][5]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I18' and second_infl='n1=out.seq.mci.I50':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I20'][6]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I18' and second_infl='n1=out.seq.mci.I60':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I20'][7]=v1v2
        except:
            continue
#----------------------------------------------------------------
    if first_infl='n1=out.seq.mci.I20' and second_infl='n1=out.seq.mci.I30':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I30'][4]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I20' and second_infl='n1=out.seq.mci.I40':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I30'][5]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I20' and second_infl='n1=out.seq.mci.I50':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I30'][6]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I20' and second_infl='n1=out.seq.mci.I60':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I30'][7]=v1v2
        except:
            continue
#------------------------------------------------
    if first_infl='n1=out.seq.mci.I30' and second_infl='n1=out.seq.mci.I40':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I30'][5]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I30' and second_infl='n1=out.seq.mci.I50':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I30'][6]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I30' and second_infl='n1=out.seq.mci.I60':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I30'][7]=v1v2
        except:
            continue
#--------------------------------------------------------------------
    if first_infl='n1=out.seq.mci.I40' and second_infl='n1=out.seq.mci.I50':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I40'][6]=v1v2
        except:
            continue
    if first_infl='n1=out.seq.mci.I40' and second_infl='n1=out.seq.mci.I60':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I40'][7]=v1v2
        except:
            continue
#-------------------------------------------
    if first_infl='n1=out.seq.mci.I50' and second_infl='n1=out.seq.mci.I60':
        try:
            value_1=re.search('[0-9]{2,6}',data[1])
            value_2=re.search('[0-9]{2,6}',data[2])
            Inflation_1=re.search('I[0-9]{1,2}', data[7])
            Inflation_2=re.search('I[0-9]{1,2}', data[8])
            v1='%s'%(value_1.group())
            v2='%s'%(value_2.group())
            I1='%s'%(Inflation_1.group())
            I2='%s'%(Inflation_2.group())
            v1v2='%s,%s'%(v1, v2)
            thedict['I50'][7]=v1v2
        except:
            continue
