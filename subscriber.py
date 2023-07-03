import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)

def show_menu():
    print("Escolha uma opção:")
    print("1. Receber mensagens individuais")
    print("2. Receber mensagens de tópicos")
    print("3. Sair")
    option = input("Opção: ")
    return option

while True:
    option = show_menu()

    if option == "1":
        recipient = input("Digite o nome do destinatário: ")
        subscription = f"RPC {recipient}"
        s.setsockopt_string(zmq.SUBSCRIBE, subscription)
    elif option == "2":
        topic = input("Digite o tópico: ")
        subscription = f"PUB {topic}"
        s.setsockopt_string(zmq.SUBSCRIBE, subscription)
    elif option == "3":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
        continue

    while True:
        message = s.recv()
        print(bytes.decode(message))

        # Verifica se o usuário deseja desconectar
        disconnect = input("Digite 'sair' para desconectar ou pressione Enter para continuar: ")
        if disconnect.lower() == "sair":
            # Remove a assinatura para desconectar do canal atual
            s.setsockopt_string(zmq.UNSUBSCRIBE, subscription)
            break

# Volta ao menu principal ou realiza outras operações
# ...


#import zmq
#from constPS import * #-

#context = zmq.Context()
#s = context.socket(zmq.SUB)          # create a subscriber socket
#p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
#s.connect(p)                         # connect to the server
#s.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages

#for i in range(5):  # Five iterations
#	time = s.recv()   # receive a message
#	print (bytes.decode(time))
