from Client0 import Client
from Seq1 import Seq
import colorama
import termcolor

PRACTICE = 2
EXERCISE = 6

print(f"-------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE}|-------")


IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
s = Seq()
s.read_fasta("../SESSION 4/FRAT1.txt")
count = 0
i = 0
while i < len(s.strbases) and count < 5:
    colorama.init(strip='False')
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print("Fragment ", count, ": ", termcolor.colored(fragment, 'blue'))
    print(c.debug_talk(fragment))