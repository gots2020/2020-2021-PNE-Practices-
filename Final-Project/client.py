import http.client
import json


def print_colored(message, color):
    from termcolor import cprint, colored
    print(colored(message, color), end="")



PORT = 8080
SERVER = '127.0.0.1'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)
list_endpoints = ["/?json=1", "/listSpecies?limit=4&json=1", "/listSpecies?limit=sdg&json=1",
                  "/karyotype?specie=homo_sapiens&json=1", "/karyotype?specie=fs2r&json=1",
                  "/chromosomeLength?specie=homo_sapiens&chromo=1&json=1", "/chromosomeLength?specie=homo_sapiens&chromo=56h6&json=1",
                  "/chromosomeLength?specie=&chromo=&json=1", "/geneSeq?gene=FRAT1&json=1", "/geneSeq?gene=gsd3r4&json=1",
                  "/geneInfo?gene=FRAT1&json=1", "/geneInfo?gene=dfs465&json=1", "/geneCalc?gene=FRAT1&json=1",
                  "/geneCalc?gene=gaagg4&json=1"]

for endpoint in list_endpoints:
    try:
        print_colored(f"Test for endpoint {endpoint}:\n", "blue")
        conn.request("GET", endpoint)
    except ConnectionRefusedError:
        print_colored("ERROR! Cannot connect to the Server", "red")
        exit()
    r1 = conn.getresponse()
    print_colored(f"Response received!: {r1.status} {r1.reason}\n", "green")
    data1 = r1.read().decode("utf-8")
    json_dict = json.loads(data1)


    print_colored(f"CONTENT:\n {json_dict}\n\n", "yellow")

