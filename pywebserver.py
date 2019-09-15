import http.server
import socketserver

print("Simple python webserver by: 545u")

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("running at port", PORT)
    httpd.serve_forever()
