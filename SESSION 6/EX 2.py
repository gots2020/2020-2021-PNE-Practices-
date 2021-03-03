import termcolor

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        termcolor.cprint("New sequence created!", "green")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def print_seqs(seq_list):
    counter = -1
    for seq in seq_list :
        counter += 1
        print("Sequence ", counter, ": ", f"(Length: {seq.len()})", f"{seq}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)