from pathlib import Path

def seq_ping():
    print("OK")

def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    return take_out_first_line(Path(filename).read_text())

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    a, c, g, t = 0, 0, 0, 0
    for e in seq :
        if e == "A":
            a += 1
        elif e == "C":
            c += 1
        elif e == "G":
            g += 1
        elif e == "T":
            t += 1
    return {"A": a, "C": c, "G": g, "T": t}

def seq_reverse(seq):
    new_string = ""
    for i in range(0, len(seq)):
        new_string += seq[len(seq) - 1 - i]
    return new_string

def seq_complement(seq):
    new_string = ""
    for e in seq:
        if e == "A":
            new_string += "T"
        elif e == "C":
            new_string += "G"
        elif e == "G":
            new_string += "C"
        elif e == "T":
            new_string += "A"
    return new_string

def frequency_base(seq):
    a, c, g, t = 0, 0, 0, 0
    for e in seq :
        if e == "A":
            a += 1
        elif e == "C":
            c += 1
        elif e == "G":
            g += 1
        elif e == "T":
            t += 1
    new_dict = {"A": a, "C": c, "G": g, "T": t}
    number_most_frequent = max(new_dict.values())
    for k, v in new_dict.items():
        if v == number_most_frequent:
            most_frequent_base = k
    return most_frequent_base
