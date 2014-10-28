for name, seq in entries:
    try:
        re.search(regex, seq) ##i think it's useless, GT
        match = re.search(regex, seq)
        motif = match.group()
        span = match.span()
        effectorname=re.search('PcRxLR..._1', name)
        print("Name: %s, Size: %s, Motif: %s, End: %s"%(effectorname,len(seq), motif, span)) # some things to see if everything is working fine: 
        splitdict[name] = int(str(span).split(", ")[1].split(")")[0])
    except: 
        print('%s, does not have a RxLR motif')%(effectorname)
        continue 
        splitdict[name] = int(str(span).split(", ")[1].split(")")[0])
