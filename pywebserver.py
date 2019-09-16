import http.server
import socketserver

print("#####################")
print("#    pywebserver    #")
print("#     Port: 80      #")
print("#     By: 545u      #")
print("#####################")

print("Port:")
PORT = input()
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server is running at port", PORT)
    httpd.serve_forever()
