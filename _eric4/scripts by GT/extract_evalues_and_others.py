import xml.etree.cElementTree as cET
fout='outfile.txt'
ofout=open(fout,'w')
for event, element in cET.iterparse('C:\Users\gt41237\Neighbourhood join\PinfvsPcapaa28.11.12.xml'):
	if 'Hit' or 'Hsp_bit-score' or 'Hsp_evalue' in element.tag:
		print>>ofout, element.text
ofout.close()
