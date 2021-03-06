# import socket programming library 
import socket
import sys 
from packet_parser import Parser
# import thread module 
from _thread import *
import threading

parser = Parser()

print_lock = threading.Lock()

stateOfApllication = True

# thread function 
def threaded(c): 
    while True: 

        # data received from client 
        data = c.recv(1024).decode() 
        if not data: 
            #print('Shutting program') 

            #parser.receive_message('bye:bye')
            print_lock.release() 
            #stateOfApllication = False
            break
        if (str(data) == 'bye:bye'):
            print('Shutting program')
            parser.receive_message('bye:bye')
            sys.exit()
        #data = data[::-1]

        print(str(data))
        parser.receive_message(str(data))


    # connection closed 
    c.close() 


def Main(): 
    host = "" 

    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 

    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 

    # a forever loop until client wants to exit 
    while True: 
        
        # establish connection with client 
        c, addr = s.accept() 

        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 

        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 


if __name__ == '__main__': 
    Main() 
