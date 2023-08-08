from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import csv

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        if self.path == "/":
            self.path = "/index.html"
        extension = self.path.split(".")[-1]
        MIME = {"html":"text/html","js":"text/javascript","css":"text/css","png":"image/png"}[extension]
        self.send_header("Content-type", MIME)
        self.end_headers()
        if self.path == "/":
            with open("index.html","rb") as f:
                self.wfile.write(f.read())
        else:
            with open(self.path.replace("%20"," ")[1:],"rb") as f:
                self.wfile.write(f.read())

    def do_POST(self):
        print("here")
        print("here")
        cLen = int(self.headers['Content-Length'])
        print(cLen)
        post_data = self.rfile.read(cLen)
        print(post_data)
        # Parse the form data
        data = json.loads(post_data.decode())
        print("Received form data:", data)


        with open("info.csv", 'a') as file:
            file.write(",".join([data["name"],data["email"],data["message"]]) + "\n")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Received the form data successfully!')

if __name__ == "__main__":
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()
