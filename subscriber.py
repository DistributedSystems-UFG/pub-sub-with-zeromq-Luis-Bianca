import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)

print("Escolha uma opção:")
print("1. Receber mensagens individuais")
print("2. Receber mensagens de tópicos")
option = input("Opção: ")

subscription = None

if option == "1":
    recipient = input("Digite o nome do destinatário: ")
    subscription = f"RPC {recipient}"
    s.setsockopt_string(zmq.SUBSCRIBE, subscription)
elif option == "2":
    topic = input("Digite o tópico: ")
    subscription = f"PUB {topic}"
    s.setsockopt_string(zmq.SUBSCRIBE, subscription)
else:
    print("Opção inválida. Por favor, tente novamente.")

while True:
    message = s.recv()
    print(bytes.decode(message))

    # Verifica se o usuário deseja desconectar
    disconnect = input("Digite algo para desconectar ou pressione Enter para continuar: ")
    if disconnect:
        # Remove a assinatura para desconectar do canal atual
        s.setsockopt_string(zmq.UNSUBSCRIBE, subscription)
        break

# Volta ao menu principal
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
