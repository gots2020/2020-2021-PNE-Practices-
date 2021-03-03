from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGTCCTG")
s3 = Seq("Incorrect sequence")

print(f"Sequence {str(1)}: (Length: {str(s1.len())}) {str(s1)}")
print(f"Sequence {str(2)}: (Length: {str(s2.len())}) {str(s2)}")
print(f"Sequence {str(3)}: (Length: {str(s3.len())}) {str(s3)}")