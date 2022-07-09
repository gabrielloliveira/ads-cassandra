from .client import Client
import argparse


def execute():
    parser = argparse.ArgumentParser(description="Parâmetros necessários.")
    parser.add_argument(
        "-n",
        "--qtd-files",
        type=int,
        action="store",
        help="Quantidade de arquivos a ser enviados para o servidor.",
        required=True,
        default=1,
    )
    parser.add_argument(
        "-z",
        "--file-size",
        help="Tamanho individual do arquivo em MB.",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-r",
        "--rate",
        help="Taxa de envio (rate).",
        type=int,
        required=True,
    )
    args = parser.parse_args()
    data = args.__dict__.copy()

    client = Client(**data)
    client.send_message()


if __name__ == "__main__":
    execute()
