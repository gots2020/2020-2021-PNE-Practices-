import termcolor
from pathlib import Path
import colorama

class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"
    def __init__(self, strbases=NULL_SEQUENCE):
        colorama.init(strip='False')
        if strbases == Seq.NULL_SEQUENCE:
            print(termcolor.colored("NULL Seq created.", 'yellow'))
            self.strbases = strbases
        else:
            if Seq.correct_seq2(strbases):
                termcolor.cprint("New sequence created.", "green")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                termcolor.cprint("ERROR!! Incorrect sequence.", "red")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    @staticmethod
    def correct_seq2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
            return True

    @staticmethod
    def generate_seqs(pattern, number):
        new_list = []
        for i in range(0, number):
            new_list.append(Seq(pattern + i*pattern))
        return new_list

    @staticmethod
    def print_seqs(seq_list):
        for i in range(0, len(seq_list)) :
            termcolor.cprint(f"Sequence {i}: (Length: {seq_list[i].len()}) {seq_list[i]}", "blue")

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not (self.strbases == Seq.NULL_SEQUENCE) and not (self.strbases == Seq.INVALID_SEQUENCE):
            for e in self.strbases:
                if e == "A":
                    a += 1
                elif e == "C":
                    c += 1
                elif e == "G":
                    g += 1
                elif e == "T":
                    t += 1
        return a, c, g, t

    @staticmethod
    def print_count_bases(bases):
        print("A: ", bases[0], ",", " C: ", bases[1], ",", " G: ", bases[2], ",",  " T: ", bases[3])

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A": a, "C": c, "G": g, "T": t}

    def reverse(self):
        rev_seq = ""
        if self.strbases == Seq.NULL_SEQUENCE:
            rev_seq = Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            rev_seq = Seq.INVALID_SEQUENCE
        else:
            for i in range(0, len(self.strbases)):
                rev_seq += self.strbases[len(self.strbases) - 1 - i]
        return rev_seq

    def complement(self):
        comp_seq = ""
        if self.strbases == Seq.NULL_SEQUENCE:
            comp_seq = Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            comp_seq = Seq.INVALID_SEQUENCE
        else:
            for e in self.strbases:
                if e == "A":
                    comp_seq += "T"
                elif e == "T":
                    comp_seq += "A"
                elif e == "G":
                    comp_seq += "C"
                elif e == "C":
                    comp_seq += "G"
        return comp_seq

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())
        return self.strbases

    def frequency_base(self):
        a, c, g, t = 0, 0, 0, 0
        for e in self.strbases:
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

    def percentage_base(self):
        a, c, g, t = self.count_bases()
        if self.len() != 0:
            p_a = round(a * 100 / self.len(), 1)
            p_c = round(c * 100 / self.len(), 1)
            p_g = round(g * 100 / self.len(), 1)
            p_t = round(t * 100 / self.len(), 1)
        return {"A: ": str(p_a) + "%", "C: ": str(p_c) + "%", "G: ": str(p_g) + "%", "T: ": str(p_t) + "%"}