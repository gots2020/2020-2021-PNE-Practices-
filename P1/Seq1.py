import termcolor

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            termcolor.cprint("NULL Seq created.", "yellow")
            self.strbases = strbases
        else:
            if Seq.correct_seq2(strbases):
                termcolor.cprint("New sequence created.", "green")
                self.strbases = strbases
            else:
                self.strbases = "ERROR"
                termcolor.cprint("ERROR!! Incorrect sequence.", "red")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
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
