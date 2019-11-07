import http.server
import socketserver

print("#####################")
print("#    pywebserver    #")
print("#    Port: 8080     #")
print("#    By: 545u       #")
print("#####################")

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server is running at port", PORT)
    httpd.serve_forever()
