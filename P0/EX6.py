import seq0

FOLDER = "./sequences/"
ID = "U5.txt"

print("-----| Exercise 6 |------")

U5_seq = seq0.seq_read_fasta(FOLDER + ID)
first_20_bases = U5_seq[0:20]

print("Frag: ", first_20_bases)
print("Rev: ", seq0.seq_reverse(first_20_bases))