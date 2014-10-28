from Bio.Align.Applications import MuscleCommandline
import os

os.chdir('D:\\Y2H\\PcRxLR252\\test')
cline = MuscleCommandline(input="test_input.txt", out="test_output.aln", clwstrict=True)
print(cline)

muscle_exe = r"C:\\Program Files\\muscle\\muscle.exe"

assert os.path.isfile(muscle_exe), "muscle executable missing"
stdout, stderr = cline()


##---

from Bio import AlignIO
alignment = AlignIO.read("test_output.aln", 'clustal')

for rec in alignment:
    print rec

    
