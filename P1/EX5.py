from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGTCCTG")
s3 = Seq("Incorrect sequence")
seq_list = [s1, s2, s3]

for i in range(1,len(seq_list) + 1):
    print(f"\nSequence {str(i)}: (Length: {str(seq_list[i - 1].len())}) {str(seq_list[i - 1])}")
    Seq.print_count_bases(seq_list[i - 1].count_bases())

