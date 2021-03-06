from Client0 import Client
from pathlib import Path
import colorama

PRACTICE = 2
EXERCISE = 5

print(f"-------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE}|-------")


IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)

colorama.init(strip='False')
print(c.debug_talk("Sending the U5 gene to the server..."))
print(c.debug_talk(Path("U5.txt").read_text()))