from .client import Client


def execute():
    client = Client()
    message_random = "123"

    while True:
        try:
            client.send_message(message_random)
        except:
            execute()


if __name__ == "__main__":
    execute()
