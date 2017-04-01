#from socket import * 
import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Prepare a sever socket 
servHost = "127.0.0.1" #socket.gethostname()
servPort = 80
serverSocket.bind((servHost, servPort))

print 'Binding to host', servHost, 'on port', servPort

packetSize = 2048

header = "Content-Type: text/html\r\n"
header += "Connection: close\r\n" 
header += "\r\n"
headerOK = "HTTP/1.1 200 OK\r\n" + header
headerNF = "HTTP/1.1 404 Not Found\r\n" + header
           
textNF = "<html><body>404 ERROR: File Not Found</body></html>"


while True: 
    #Establish the connection 
    print 'Ready to serve...'
    serverSocket.listen(5)
    connectionSocket, addr = serverSocket.accept() 
    try:
        message =  connectionSocket.recv(packetSize)
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read() 
        print 'Filename: ', filename
        print 'OutputData: ', outputdata
        #Send one HTTP header line into socket 
        connectionSocket.send(headerOK)

        #for i in range(0, len(outputdata)): 
        connectionSocket.send(outputdata) 
        connectionSocket.close() 
    except IOError: 
        #Send response message for file not found 
        connectionSocket.send(headerNF)
        connectionSocket.send(textNF)
        #Close client socket 
        connectionSocket.close()
