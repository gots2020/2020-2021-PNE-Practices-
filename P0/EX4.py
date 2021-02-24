import seq0

GENE_FOLDER = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list =["A", "C", "T", "G"]

print("-----| Exercise 4 |------")
for gene in gene_list:
    sequence = seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene", gene)
    for base in base_list :
        print(base + ": " + str(seq0.seq_count_base(sequence, base)))