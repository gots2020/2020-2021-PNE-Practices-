from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-------|PRACTICE {PRACTICE}, EXERCISE {EXERCISE}|-------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

print("Testing GET...")
print(c.talk("GET 0"))
print(c.talk("GET 1"))
print(c.talk("GET 2"))
print(c.talk("GET 3"))
print(c.talk("GET 4"))