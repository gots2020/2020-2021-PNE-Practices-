from Seq1 import Seq
import jinja2
import pathlib
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

def get(list_sequences, seq_number):
    context = {"number": seq_number, "sequence": list_sequences[int(seq_number)]}
    content = read_template_html_file("./html/get.html").render(context=context)
    return content

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

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

def gene(seq_name):
    PATH = "./sequences/" + seq_name + ".txt"
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {"gene_name": seq_name, "gene_contents": s1.strbases}
    content = read_template_html_file("./html/gene.html").render(context=context)
    return content



