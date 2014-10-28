Bout=open('C:\Users\gt41237\Neighbourhood join\PinfvsPcapdb22.11.12.xml','r')
from Bio.Blast import NCBIStandalone
b_parser = NCBIStandalone.BlastParser()
b_iterator = NCBIStandalone.Iterator(Bout, b_parser)
b_record = b_iterator.next()
while 1:
    b_record = b_iterator.next()
    if b_record is None:
        break
E_VALUE_THRESH = 0.04
for alignment in b_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print '****Alignment****'
            print 'sequence:', alignment.title
            print 'length:', alignment.length
            print 'e value:', hsp.expect
            if len(hsp.query) > 75:
                dots = '...'
            else:
                dots = ''
            print hsp.query[0:75] + dots
            print hsp.match[0:75] + dots
            print hsp.sbjct[0:75] + dots
