from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE}|-------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

print("Testing GENE...")
print(c.talk("GENE U5"))
print(c.talk("GENE ADA"))
print(c.talk("GENE FRAT1"))
print(c.talk("GENE FXN"))
print(c.talk("GENE RNU6_269P"))
