import seq0

GENE_FOLDER = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 5 |------")
for gene in gene_list:
    sequence = seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene ", gene, ": " , seq0.seq_count(sequence))