from socket import * 
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket 
servHost = serverSocket.gethostname()
servPort = 80
serverSocket.bind((servHost, servPort))

packetSize = 2048

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
        #Send one HTTP header line into socket 
        connectionSocket.send('HTTP/1.1 200 OK')
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i]) 
        connectionSocket.close() 
    except IOError: 
        #Send response message for file not found 
        connectionSocket.send('HTTP/1.1 404 Not Found')
        #Close client socket 
        connectionSocket.close()

