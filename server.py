import socket
import threading

# application - sets up the port number for the app data
# presentation - defines the data formatting for the port
port = 5001 

# transport - creates a socket using tcp (Transmission Control Protocol) forconnection
device = socket.socket() 

# session - starts session by identifying server or client
if input("Are you a the main server pc? (y/n): ") == "y":
    
    # network - connects the socket with ip so it can route using path determination and logical addressing
    # data link - relates script with network through pc hardware using frames
    device.bind(('', port)) 
    
    # session - listens and waits for communication to open the data connection
    device.listen() 
    print("Waiting for your bro to connect...") 
    chat, address = device.accept() 
    
else:
    # network - connects the socket with ip so it can route packets across the network path
    # physical - transmits raw bits as signals over physical media like wires or wifi
    device.connect((input("Server IP: "), port)) 
    chat = device 

# session - manages a background thread for interhost communication data transfer
def listen():
    while True:
        # presentation - translates binary data bytes into readable text characters
        message = chat.recv(1024).decode() 
        
        if not message: 
            break
            
        # application - displays the final data on the network process user screen
        print("\nBro: ", message) 

threading.Thread(target=listen, daemon=True).start()

# application - handles the network process to application user chat loop
while True:
    message = input("You: ") 
    
    if message == "/quit": 
        break
        
    # presentation - converts text characters into binary data formatting for transmission
    chat.sendall(message.encode()) 

# session - brings down the interhost communication to close the chat
chat.close() 
