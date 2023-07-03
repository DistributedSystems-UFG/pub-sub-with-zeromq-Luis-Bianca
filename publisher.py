import zmq
import time
from constPS import *

context = zmq.Context()
s = context.socket(zmq.PUB)
p = "tcp://" + HOST + ":" + PORT
s.bind(p)

while True:
    # Exibe o menu de opções para o usuário
    print("Escolha uma opção:")
    print("1. Enviar mensagem individual")
    print("2. Enviar mensagem para tópico")
    print("3. Sair")
    option = input("Opção: ")

    if option == "1":
        # Solicita ao usuário o nome do destinatário e a mensagem
        recipient = input("Digite o nome do destinatário: ")
        message = input("Digite a mensagem: ")
        # Monta a mensagem usando "RPC" para identificar que é uma mensagem individual
        msg = str.encode(f"RPC {recipient} {message}")
        # Envia a mensagem
        s.send(msg)
    elif option == "2":
        # Solicita ao usuário o tópico e a mensagem
        topic = input("Digite o tópico: ")
        message = input("Digite a mensagem: ")
        # Monta a mensagem usando "PUB" para identificar que é uma mensagem de tópico
        msg = str.encode(f"PUB {topic} {message}")
        s.send(msg)
    elif option == "3":
        # Encerra a aplicação
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
