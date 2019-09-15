import http.server
import socketserver

print("Simple python webserver running on port 80 by: 545u")

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("running at port", PORT)
    httpd.serve_forever()
