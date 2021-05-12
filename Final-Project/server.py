import http.server
import http.client
import json
import socketserver
import termcolor
import jinja2
import pathlib
from urllib.parse import urlparse, parse_qs

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

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)


        print("Resource requested: ", path_name)
        print("Parameters:", arguments)


        SERVER = "rest.ensembl.org"
        PARAMETERS = "?content-type=application/json"
        connection = http.client.HTTPConnection(SERVER)

        context = {}
        if path_name == "/":
            contents = read_template_html_file("./HTML/index.html").render()
        elif path_name == "/listSpecies":
            try:
                ENDPOINT = "/info/species"
                connection.request("GET", ENDPOINT + PARAMETERS)
                response = connection.getresponse()
                response_dict = json.loads(response.read().decode())
                count = len(response_dict["species"])
                new_list = []
                try:
                    if 0 <= int(arguments["limit"][0]) <= 310:
                        for i in range(0, int(arguments["limit"][0])):
                            new_list.append(response_dict["species"][i]["common_name"])
                        context = {"Total_seq": count,
                                   "limit": arguments["limit"][0],
                                   "names_seq": new_list}
                        contents = read_template_html_file("./HTML/listSpecies.html").render(context=context)
                    elif int(arguments["limit"][0]) > 310:
                        for i in range(0, 310):
                            new_list.append(response_dict["species"][i]["common_name"])
                        context = {"Total_seq": count,
                                   "limit": arguments["limit"][0],
                                   "names_seq": new_list}
                        contents = read_template_html_file("./HTML/listSpecies.html").render(context=context)
                    else:
                        contents = read_template_html_file("./HTML/error_limit.html").render()
                except KeyError:
                    for i in range(0, 310):
                        new_list.append(response_dict["species"][i]["common_name"])
                    context = {"Total_seq": count,
                               "limit": "None",
                               "names_seq": new_list}
                    contents = read_template_html_file("./HTML/listSpecies.html").render(context=context)
            except ValueError:
                contents = read_template_html_file("./HTML/error_limit.html").render()
        elif path_name == "/karyotype":
            specie = arguments["specie"][0].replace(" ", "_")
            ENDPOINT = "/info/assembly/" + specie
            connection.request("GET", ENDPOINT + PARAMETERS)
            response = connection.getresponse()
            if response.status == 200:
                response_dict = json.loads(response.read().decode())
                context = {"Chromosome_names": response_dict["karyotype"]}
                contents = read_template_html_file("./HTML/karyotype.html").render(context=context)
            else:
                contents = read_template_html_file("./HTML/error_specie.html").render()
        elif path_name == "/chromosomeLength":
            try:
                specie = arguments["specie"][0].replace(" ", "_")
                ENDPOINT = "/info/assembly/" + specie
                connection.request("GET", ENDPOINT + PARAMETERS)
                response = connection.getresponse()
                if response.status == 200:
                    response_dict = json.loads(response.read().decode())
                    new_list = response_dict["top_level_region"]
                    for d in new_list:
                        if d["name"] == arguments["chromo"][0]:
                            context = {"Chromosome_length": d["length"]}
                    contents = read_template_html_file("./HTML/chromosomeLength.html").render(context=context)
                else:
                    contents = read_template_html_file("./HTML/error_specie.html").render()
            except KeyError:
                contents = read_template_html_file("./HTML/error_specie.html").render()
        else:
            contents = read_template_html_file("./HTML/error.html").render()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
