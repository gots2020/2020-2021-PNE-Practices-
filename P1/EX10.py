from Seq1 import Seq

s1 = Seq()
s1.read_fasta("./sequences/" + "U5.txt")
print("Gene U5", ": " , "Most frequent base : ", s1.frequency_base())

s2 = Seq()
s2.read_fasta("./sequences/" + "ADA.txt")
print("Gene ADA", ": " , "Most frequent base : ", s2.frequency_base())

s3 = Seq()
s3.read_fasta("./sequences/" + "FRAT1.txt")
print("Gene FRAT1", ": " , "Most frequent base : ", s3.frequency_base())

s4 = Seq()
s4.read_fasta("./sequences/" + "FXN.txt")
print("Gene FXN", ": " , "Most frequent base : ", s4.frequency_base())

s5 = Seq()
s5.read_fasta("./sequences/" + "RNU6_269P.txt")
print("Gene RNU6_269P", ": " , "Most frequent base : ", s5.frequency_base())
