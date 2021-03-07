from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGTCCTG")
s3 = Seq("Incorrect sequence")

print(f"\nSequence {str(0)}: (Length: {str(s1.len())}) {str(s1)}")
print("  Bases: ", s1.count())
print("  Rev:   ", s1.reverse())
print("  Comp:  ", s1.complement())

print(f"Sequence {str(1)}: (Length: {str(s2.len())}) {str(s2)}")
print("  Bases: ", s2.count())
print("  Rev:   ", s2.reverse())
print("  Comp:  ", s2.complement())

print(f"Sequence {str(2)}: (Length: {str(s3.len())}) {str(s3)}")
print("  Bases: ", s3.count())
print("  Rev:   ", s3.reverse())
print("  Comp:  ", s3.complement())