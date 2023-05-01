"""Tcp server module
"""

import socket
from constant import Constant

def main():
    """fn to start the server and echo the data
    """
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.bind(Constant.Config.SERVER_ADDRESS)
    socket_.listen(1)
    while True:
        print("waiting for connection")
        connection, client_address = socket_.accept()
        print(f"Connection created on address: {client_address}")
        try:
            while True:
                data = connection.recv(Constant.Config.BUFFER_SIZE)
                print("Data received: ", data)  
                if data:
                    # send the data back
                    connection.send(data)
                else:
                    print("No data from connection")
                    break
        finally:
            # close connection in end
            connection.close()

if __name__ == "__main__":
    print("Starting the server")
    main()