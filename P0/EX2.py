import seq0

FOLDER = "./sequences/"
ID = "U5.txt"

U5_seq = seq0.seq_read_fasta(FOLDER + ID)
print("The first 20 bases are: ", U5_seq[0:20])
