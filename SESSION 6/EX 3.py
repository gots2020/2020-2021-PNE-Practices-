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

def generate_seqs(pattern, number):
    new_list = []
    for i in range(0, number ):
        element = Seq(pattern + i*pattern)
        new_list.append(element)
    return new_list

def print_seqs(seq_list):
    counter = -1
    for seq in seq_list :
        counter += 1
        print("Sequence ", counter, ": ", f"(Length: {seq.len()})", f"{seq}")


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("\nList 1:", "blue")
print_seqs(seq_list1)

termcolor.cprint("\nList 2:", "blue")
print_seqs(seq_list2)
