import http.client
import json


def print_colored(message, data, color):
    from termcolor import cprint, colored
    print(colored(message, color), end="")
    print(data)

genes_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

PORT = 8080
SERVER = '127.0.0.1'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)
try:
    conn.request("GET", "/?json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
json_string = json.dumps(data1)
json_dict = json.loads(json_string)

print(f"CONTENT:\n {json_dict}")

