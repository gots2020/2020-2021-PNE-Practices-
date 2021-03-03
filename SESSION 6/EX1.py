import termcolor

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        for c in strbases:
            if c != "A" and c != "C" and c != "G" and c != "T" :
                self.strbases = "ERROR"
                termcolor.cprint("ERROR!!", "red")
                break
            else:
                self.strbases = strbases
    termcolor.cprint("New sequence created.", "green")


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.strbases


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
