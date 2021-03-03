from seq_01 import Seq
import termcolor

seq_list1 = Seq.generate_seqs("A", 3)
seq_list2 = Seq.generate_seqs("AC", 5)

termcolor.cprint("\nList 1:", "blue")
Seq.print_seqs(seq_list1)

termcolor.cprint("\nList 2:", "blue")
Seq.print_seqs(seq_list2)
