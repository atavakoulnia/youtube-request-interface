import socket
import pickle

FORMAT = 'utf-8'

#create a client 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5721))
print("Connecting to server")
print("Sending request")

#function to receive reply from server
def receive():
    msg = s.recv(1024)
    data = pickle.loads(msg)    #serialize using pickle
    print(data)

#function to send request to server
def send(msg):
    data = pickle.dumps(msg)
    s.send(data)

send(["free guys"]) # input the name of the movie
receive()

