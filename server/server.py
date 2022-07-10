import socket
from tempfile import NamedTemporaryFile
from .cassandra import CassandraDriver

SERVER_ADDRESS = ("0.0.0.0", 8080)
BUFFER_SIZE = 1024 // 2
FINISHED_MESSAGE = b"DONE"
FILE_COMPLETED = b"COMPLETED"


bd = CassandraDriver()


class Server:
    def __init__(self):
        self.address = SERVER_ADDRESS
        self.sock = self.__create_sock()

    def __create_sock(self):
        """
        Create TCP server socket
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.address)
        return sock

    def run(self):
        """Run the server."""
        print("🚀 Starting server on mode partner...")
        print(f"🚀 Starting server on address {self.address}...")
        self.listen()

    def listen(self):
        """Listen for connections."""
        self.sock.listen()
        # TODO: pegar o consumo de memória e cpu
        while True:
            conn, client_address = self.sock.accept()
            print("‍💼 Received connection from SERVER...", client_address)
            message = conn.recv(BUFFER_SIZE)
            file_parts = []

            while message:
                if str(message) == str(FINISHED_MESSAGE):
                    print("All Files Received")
                    break

                if str(message) == str(FILE_COMPLETED):
                    print("File Received")
                    file_data = "".join(file_parts)
                    bd.create(file_data=file_data.encode())
                    file_parts = []
                    message = b""
                    conn.send("OK".encode())

                message = message.decode("utf-8")
                print("Receiving...")
                file_parts.append(message)
                message = conn.recv(BUFFER_SIZE)

            file_parts = []
            response_data = "OK"
            conn.send(str(response_data).encode())
