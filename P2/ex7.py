from Client0 import Client
import termcolor
from Seq1 import Seq
import colorama

PRACTICE = 2
EXERCISE = 6

print(f"-------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE}|-------")


IP = "127.0.0.1"
PORT = 12000
PORT2 = 12300

c = Client(IP, PORT)
c_2 = Client(IP, PORT2)
s = Seq()
s.read_fasta("../SESSION 4/FRAT1.txt")
count = 0
i = 0
colorama.init(strip='False')

print(c_2.debug_talk("Sending FRAT1 gene to server1, in fragments of 10 bases..."))
print(c.debug_talk("Sending FRAT1 gene to server2, in fragments of 10 bases..."))
print("Gene FRAT1: ", termcolor.colored(s, 'blue'))

while i < len(s.strbases) and count < 10:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print("Fragment ", count, ": ", termcolor.colored(fragment, 'blue'))
    if count % 2 == 0:
        print(c_2.debug_talk("Fragment " + str(count) + ": " + fragment))
    else:
        print(c.debug_talk("Fragment " + str(count) + ": " + fragment))
