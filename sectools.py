
import socket
def serverSocket():
    # Create a TCP Server: 

    #Import socket from socket library, set Address Family to IPv4 
    #  using mode TCP (Sock-stream).
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Grab the hostname
    host = socket.gethostbyname() 
    port = 444

    serversocket.bind(host, port)   # Double brackets used in Video

    serversocket.listen(3)    # Create a "Lisenter" and specify how many.

    while True:
        # Starting the connection
        clientsocket, address = serversocket()

        print("Receieved a connection from %s" % address)

        message = "Hello! Thank you for connecting to the server. \n"
        clientsocket.send(message.encode('ascii'))

        clientsocket.close()

def scan(target_ip, number_of_ports):
    for port in range(1, number_of_ports):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print("Port {}: Open".format(port))
            sock.close()
            
def newfunction():
    pass
