import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)

def show_menu():
    # Exibe o menu de opções para o usuário
    print("Escolha uma opção:")
    print("1. Receber mensagens individuais")
    print("2. Receber mensagens de tópicos")
    print("3. Sair")
    option = input("Opção: ")
    return option

while True:
    option = show_menu()

    if option == "1":
        # Solicita ao usuário o nome
        recipient = input("Digite o nome do destinatário: ")
        # Monta a assinatura "RPC" para receber mensagens individuais
        subscription = f"RPC {recipient}"
        # Define a assinatura no socket para receber mensagens do destinatário especificado
        s.setsockopt_string(zmq.SUBSCRIBE, subscription)
    elif option == "2":
        # Solicita ao usuário o tópico
        topic = input("Digite o tópico: ")
        # Monta a assinatura "PUB" para receber mensagens de tópico
        subscription = f"PUB {topic}"
        # Define a assinatura no socket para receber mensagens do tópico especificado
        s.setsockopt_string(zmq.SUBSCRIBE, subscription)
    elif option == "3":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
        continue

    while True:
        # Recebe a mensagem do socket
        message = s.recv()
        print(bytes.decode(message))

        # Verifica se o usuário deseja desconectar
        disconnect = input("Digite 'sair' para desconectar ou pressione Enter para continuar: ")
        if disconnect.lower() == "sair":
            # Remove a assinatura para desconectar do canal atual
            s.setsockopt_string(zmq.UNSUBSCRIBE, subscription)
            # Encerra a aplicação
            break
