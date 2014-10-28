fileout=open('C:\Users\gt41237\MCLINSTRUCTION', 'wb')
count=1
while count<51:
    print>>fileout, "cut -f 1,2,11 /cygdrive/c/Users/gt41237/JackKnives/JackKnifeDict_%s_selfblastp > JKDict%s.abc" %(count, count)
    print>>fileout, "mcxload -abc JKDict%s.abc --stream-mirror --stream-neg-log10 -stream-tf 'ceil(200)' -o JKDict%s.mci -write-tab JKDict%s.tab"%(count, count, count)
    print>>fileout, 'mcl JKDict%s.mci -I 2'%(count)
    print>>fileout, 'mcl JKDict%s.mci -I 4'%(count)
    print>>fileout, 'mcl JKDict%s.mci -I 6'%(count)
    print>>fileout, 'mcxdump -icl out.JKDict%s.mci.I20 -tabr JKDict%s.tab -o dump.JKDict%s.mci.I20'%(count, count, count)
    print>>fileout, 'mcxdump -icl out.JKDict%s.mci.I40 -tabr JKDict%s.tab -o dump.JKDict%s.mci.I40'%(count, count, count)
    print>>fileout, 'mcxdump -icl out.JKDict%s.mci.I60 -tabr JKDict%s.tab -o dump.JKDict%s.mci.I60'%(count, count, count)
    count=count+1
