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
list_endpoints = ["/?json=1", "/listSpecies?limit=4&json=1", "/listSpecies?limit=sdg&json=1",
                  "/karyotype?specie=homo_sapiens?json=1", "/karyotype?specie=fs2r?json=1",
                  "/chromosomeLength?specie=homo_sapiens&chromo=1?json=1", "/chromosomeLength?specie=homo_sapiens&chromo=56h6?json=1",
                  "/chromosomeLength?specie=&chromo=?json=1", "/geneSeq?gene=FRAT1&json=1", "/geneSeq?gene=gsd3r4&json=1",
                  "/geneInfo?gene=FRAT1&json=1", "/geneInfo?gene=dfs465&json=1", "/geneCalc?gene=FRAT1&json=1",
                  "/geneCalc?gene=gaagg4&json=1"]

for endpoint in list_endpoints:
    try:
        print(f"Test for endpoint {endpoint}:\n")
        conn.request("GET", endpoint)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    json_string = json.dumps(data1)
    json_dict = json.loads(json_string)

    print(f"CONTENT:\n {json_dict}\n")

