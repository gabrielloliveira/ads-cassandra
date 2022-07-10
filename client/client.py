import logging
import os
import socket
import time
import random
import string

SERVER_ADDRESS = ("0.0.0.0", 8080)
BUFFER_SIZE = 1024 * 1
ONE_MB = 1024 * 1024
FINISHED_MESSAGE = b"DONE"
COMPLETED_FILE = b"COMPLETED"


logging.basicConfig(filename="client.log", encoding="utf-8", level=logging.INFO)


class Client:
    def __init__(self, **kwargs):
        self.server_address = SERVER_ADDRESS
        self.qtd_files = kwargs.get("qtd_files")
        self.file_size = kwargs.get("file_size")
        self.rate = kwargs.get("rate")

    def send_message(self):
        list_files = self.__prepare_files()

        server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        server.connect(self.server_address)
        print(f"✅ TCP CONNECTION WITH SERVER: {self.server_address}")

        for file in list_files:
            start_time = time.time()
            print(f"🔁 SENDING FILE {file} TO SERVER")

            f = open(file, "rb")
            buffer = f.read(BUFFER_SIZE)
            while buffer:
                server.send(buffer)
                buffer = f.read(BUFFER_SIZE)

            server.send(COMPLETED_FILE)
            f.close()
            print(f"✅ FILE {file} WAS SENT")

            response = server.recv(BUFFER_SIZE)
            message = response.decode("utf-8")
            final_time = time.time() - start_time
            print(f"📨 Received response: {message} in {final_time} seconds")
            logging.info(f"RESPONSE-TIME={final_time}")
            time.sleep(self.rate)

        server.send(FINISHED_MESSAGE)
        server.recv(BUFFER_SIZE)
        server.close()
        self.__remove_files(list_files)

    def __prepare_files(self) -> list:
        """
        Generate files and return list with filenames
        """
        print(f"🔁 GENERATING {self.qtd_files} FILES WITH SIZE {self.file_size} MB")
        size = ONE_MB * self.file_size
        chars = "".join([random.choice(string.ascii_letters) for i in range(size)])

        filenames = []

        for i in range(self.qtd_files):
            filename = f"{i+1}.txt"
            filenames.append(filename)

            with open(filename, "w") as f:
                f.write(chars)
        print(f"✅ ALL FILES WAS GENERATED: {filenames}")
        return filenames

    @staticmethod
    def __remove_files(list_filenames):
        """Exclude all files from disk"""
        for file in list_filenames:
            os.remove(file)
