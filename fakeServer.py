import socket

HOST = '127.0.0.1'  
PORT = 5050         

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))     
server.listen(1)             
print(f"[+] Listening on {HOST}:{PORT}...")

try:
    while True:
        client_socket, address = server.accept()
        print(f"[+] Got connection from {address}")
        client_socket.send(b"Hello!\n")
        client_socket.close()
except KeyboardInterrupt:
    print("\n[!] Shutting down server.")
    server.close()
