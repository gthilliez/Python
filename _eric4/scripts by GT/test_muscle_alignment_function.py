


def MuscleAlignment(Input, Output, PathToMuscle='C:\\Program Files\\muscle\\muscle.exe'):
    """COMMENTS
    Based on the tutorial for biopython available here http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec77
    Input is path to a fasta file
    Output is name of a file that will be created by the funcion and will contain the output alignment
    PathTomuscle is a path to the muscle executable (available here : http://www.drive5.com/muscle/downloads.htm)"""
    from Bio.Align.Applications import MuscleCommandline
    import os
    cline = MuscleCommandline(input=Input, out=Output, clwstrict=True)
    muscle_exe = PathToMuscle
    assert os.path.isfile(muscle_exe), "muscle executable missing; please check the path to muscle %s"%PathToMuscle
    stdout, stderr = cline()
