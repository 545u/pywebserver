import http.server
import socketserver

print("#####################")
print("#    pywebserver    #")
print("# Default port: 80  #")
print("#      By: 545u     #")
print("#####################")

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("running at port", PORT)
    httpd.serve_forever()
