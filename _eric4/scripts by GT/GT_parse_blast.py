def GT_parse_blast(Blast_output):
    import xml.etree.cElementTree as cET
    import os
    while True:
        oname= raw_input('Enter output filename: ')
        ofout=open(oname,'w')
        if os.path.exists(oname):
            print'outfile ok'
        else:
            print('Output file is not writable, check that the path of the file is correct and that Python have the right to modify the destination folder')
        iname= raw_input('Enter path to blastoutput.xml: ')
        if os.path.exists(iname):
            iname_o=open(iname)
            for event, element in cET.iterparse(iname_o):
                if 'Hit' or 'Hsp_bit-score' or 'Hsp_evalue' in element.tag:
                    print>>ofout, element.text
                else:
                    print 'there is no hit in this blast output'
	
        else:
            print 'There is a problem with the blast_output, invalide path or file'
        ofout.close()
