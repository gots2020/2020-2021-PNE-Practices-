from Client0 import Client
import colorama

PRACTICE = 2
EXERCISE = 4

print(f"-------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE}|-------")


IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)

colorama.init(strip='False')

print(c.debug_talk("Message 1---"))
print(c.debug_talk("Message 2: Testing !!!"))