from P1 import Seq1
from Seq1 import Seq
from P1 import sequences

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip=False)
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")
def ping(cs):
    print_colored("PING command!", "green")
    print("OK!")
    response = "OK!"
    cs.send(str(response).encode())

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())


def info(cs, sequence):
    print_colored("INFO", "yellow")
    s = Seq(sequence)
    total_len = s.len()
    a, c, g, t = s.count_bases()
    p_a, p_c, p_g, p_t = 0, 0, 0, 0
    if total_len != 0:
        p_a = round(a * 100/ total_len, 1)
        p_c = round(c * 100/ total_len, 1)
        p_g = round(g * 100/ total_len, 1)
        p_t = round(t * 100/ total_len, 1)
    response = "Sequence: " + sequence + "\nTotal length: " + str(total_len) + "\nA: " + str(a) + " (" + str(p_a) + "%" + ")" + "\nC: " + str(c) + " (" + str(p_c) + "%" + ")" + "\nG: " + str(g) + " (" + str(p_g) + "%" + ")" + "\nT: " + str(t) + " (" + str(p_t) + "%" + ")"
    print(response)
    cs.send(response.encode())

def comp(cs, sequence):
    print_colored("COMP", "yellow")
    s = Seq(sequence)
    response = s.complement()
    print(response)
    cs.send(response.encode())

def rev(cs,sequence):
    print_colored("REV", "yellow")
    s = Seq(sequence)
    response = s.reverse()
    print(response)
    cs.send(response.encode())

def gene(cs, argument):
    s = Seq()
    filename = "../P1/sequences/" + argument + ".txt"
    print_colored("GENE", "yellow")
    try:
        response = s.read_fasta(filename)
        print(response)
        cs.send(response.encode())
    except FileNotFoundError:
        response = "File not found."
        print(response)
        cs.send(response.encode())

