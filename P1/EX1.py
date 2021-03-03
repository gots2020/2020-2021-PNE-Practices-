from Seq1 import Seq
import termcolor

termcolor.cprint("-----| Exercise 1 |------", "yellow")
seq = Seq("ACTGA")
termcolor.cprint(f"Sequence {str(1)}: (Length: {str(seq.len())}) {str(seq)}", "blue")