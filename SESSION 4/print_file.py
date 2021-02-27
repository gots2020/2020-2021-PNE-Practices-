FILENAME = "RNU6_269P.txt"
GENE_FOLDER = "../P0/sequences/"

# -- Open and read the file
with open(GENE_FOLDER + FILENAME) as f:
    text = f.read()
    lines = text.split("\n")
    print(lines[0])



