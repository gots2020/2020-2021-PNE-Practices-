from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE}|-------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

print("Testing PING...")
print(c.talk("PING"))