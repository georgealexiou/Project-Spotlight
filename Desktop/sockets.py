import socket
from packet_parser import Parser
import threading

parser = Parser()

def server_program():
    # get the hostname
    host = ''
    port = 8888  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    conn, address = server_socket.accept()  # accept new connection
    #print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        #print(str(data) is 'Cursor_Move:0.5,0.5')
        #print(len(data))
        #print("from connected user: {}".format(str(data)))
        ##if not data:
            # if data is not received break
            #break

        if str(data) == 'bye':
            print("Bye!")
            conn.close()
            break

        elif len(data) == 0:
            
            continue

        else:
            #threads = []
            #t = threading.Thread(target=parser.receive_message, args=(str(data),))
            #threads.append(t)
            #t.start()
            #t.join()
            parser.receive_message(str(data))
            print("message received: {}".format(str(data)))
        
        # data = input(' -> ')
        # conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()