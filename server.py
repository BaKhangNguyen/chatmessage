import socket
import threading

port = 5001
device = socket.socket()
if input("Are you a Host? (y/n): ") == "y":
    device.bind(("", port))
    device.listen()
    print("Waiting for connection...")
    chat, address = device.accept()
else:
    device.connect((input("Server IP: "), port))
    chat = device

def listen():
    while True:
        message = chat.recv(1024).decode()
        if not message:
            break
        print("\nFriend:", message)

threading.Thread(target=listen, daemon=True).start()

while True:
    message = input("You: ")
    if message == "/quit":
        break
    chat.sendall(message.encode())

chat.close()
