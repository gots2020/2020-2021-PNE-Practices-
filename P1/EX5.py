from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGTCCTG")
s3 = Seq("Incorrect sequence")

print(f"\nSequence {str(0)}: (Length: {str(s1.len())}) {str(s1)}")
Seq.print_count_bases(s1.count_bases())

print(f"Sequence {str(1)}: (Length: {str(s2.len())}) {str(s2)}")
Seq.print_count_bases(s2.count_bases())

print(f"Sequence {str(2)}: (Length: {str(s3.len())}) {str(s3)}")
Seq.print_count_bases(s3.count_bases())