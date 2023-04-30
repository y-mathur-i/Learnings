import socket
import sys

SERVER_ADDRESS = ("localhost", 8008)
BUFFER_SIZE = 16

def main():
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_.bind(SERVER_ADDRESS)
    socket_.listen(1)
    while True:
        print("waiting for connection")
        connection, client_address = socket_.accept()
        print(f"Connection created on address: {client_address}")
        try:
            while True:
                data = connection.recv(BUFFER_SIZE)
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