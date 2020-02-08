import socket
import packet_parser import Parser

parser = Parser()

def server_program():
    # get the hostname
    host = ''
    port = 8888  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind(('', port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        elif data == 'bye':
            conn.close()
            
        parser.receive_message(str(data))
        print("from connected user: " + str(data))
        # data = input(' -> ')
        # conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()