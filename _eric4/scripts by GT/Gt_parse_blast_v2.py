from Bio.Blast import NCBIXML
while True:
        oname= raw_input('Enter output filename: ')
        ofout=open(oname,'w')
        if os.path.exists(oname):
            print'outfile ok'
        else:
            print('Output file is not writable, check that the path of the file is correct and that Python have the right to modify the destination folder')
        iname= raw_input('Enter path to blastoutput.xml: ')
        try:
            iname_o=open(iname)
        except:
            print ("There is a problem with the blast output, file doesn't exist or wrong format")
        blast_parsing = NCBIXML.parse(iname_o)
       #blast_records = g(blast_parsing)
        for alignment in blast_parsing.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    print '****Alignment****'
                    print 'sequence:', alignment.title
                    print 'length:', alignment.length
                    print 'e value:', hsp.expect
