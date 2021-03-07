from Seq1 import Seq

s = Seq()
s.read_fasta("./sequences/" + "U5.txt")



print(f"\nSequence : (Length: {str(s.len())}) {str(s)}")
print("  Bases: ", s.count())
print("  Rev:   ", s.reverse())
print("  Comp:  ", s.complement())