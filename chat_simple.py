from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import threading


class Chat(BaseHTTPRequestHandler):
    def do_POST(self):
        size = int(self.headers["Content-Length"])
        message = self.rfile.read(size).decode("utf-8")
        print(f"\nFriend: {message}\nYou: ", end="", flush=True)
        self.send_response(200)
        self.end_headers()

    def log_message(self, *args):
        pass


def listen():
    HTTPServer(("0.0.0.0", 5000), Chat).serve_forever()


threading.Thread(target=listen, daemon=True).start()
friend_ip = input("Friend's IPv4 address: ")

while True:
    message = input("You: ")
    if message == "/quit":
        break

    body = message.encode("utf-8")
    header = (f"POST /chat HTTP/1.1\r\n"
              f"Host: {friend_ip}\r\n"
              f"Content-Length: {len(body)}\r\n"
              f"Connection: close\r\n\r\n")

    try:
        with socket.create_connection((friend_ip, 5000), timeout=5) as s:
            s.sendall(header.encode("utf-8") + body)
            print(s.recv(1024).decode().splitlines()[0])
    except OSError as error:
        print("Connection failed:", error)
