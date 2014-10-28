import subprocess
count=1
while count < 101:
    print 'now blasting %s %s and %s'%(count, count+1, count+2)
    filepath='C:\Users\gt41237\Cluster_on_RxLRs_only\JackKnife_dict_Pi_Pc_Ps_EER_trunc\JackKnifeDictRxLR_%s'%(count)
    fileoutpath='C:\Users\gt41237\Cluster_on_RxLRs_only\SelfBlastJackKnifeDictRxLR_%s'%(count)
    testsub1=subprocess.Popen(['blastp', '-query',filepath, '-db', filepath, '-evalue', '1e-5','-outfmt', '6','-out', fileoutpath])
    count=count+1
    filepath='C:\Users\gt41237\Cluster_on_RxLRs_only\JackKnife_dict_Pi_Pc_Ps_EER_trunc\JackKnifeDictRxLR_%s'%(count)
    fileoutpath='C:\Users\gt41237\Cluster_on_RxLRs_only\SelfBlastJackKnifeDictRxLR_%s'%(count)
    testsub2=subprocess.Popen(['blastp', '-query',filepath, '-db', filepath, '-evalue', '1e-5','-outfmt', '6','-out', fileoutpath])
    count=count+1
    filepath='C:\Users\gt41237\Cluster_on_RxLRs_only\JackKnife_dict_Pi_Pc_Ps_EER_trunc\JackKnifeDictRxLR_%s'%(count)
    fileoutpath='C:\Users\gt41237\Cluster_on_RxLRs_only\SelfBlastJackKnifeDictRxLR_%s'%(count)
    testsub3=subprocess.Popen(['blastp', '-query',filepath, '-db', filepath, '-evalue', '1e-5','-outfmt', '6','-out', fileoutpath])
    count=count+1
    testsub3.wait()
    if count == 101:
        print "over"
        break
    print "Done for those 3"

