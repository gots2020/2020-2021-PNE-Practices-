def count_dna(seq):
    a = 0
    c = 0
    g = 0
    t = 0
    for e in seq:
        if e == "A":
            a += 1
        elif e == "C":
            c += 1
        elif e == "G":
            g += 1
        elif e == "T":
            t += 1
    return a, c, g, t

def read_from_file(filename):
    f = open(filename, "r")
    dna = f.read()
    dna = dna.replace("\n", "")
    return dna

seq = read_from_file("dna.txt")
print("TOTAL LENGTH : " , len(seq))
a, c, g, t = count_dna(seq)
print(  "A : ", a,
        "\nC : ", c,
        "\nG : ", g,
        "\nT : ", t)