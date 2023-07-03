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

if option == "1":
    recipient = input("Digite o nome do destinatário: ")
    s.setsockopt_string(zmq.SUBSCRIBE, f"RPC {recipient}")
elif option == "2":
    topic = input("Digite o tópico: ")
    s.setsockopt_string(zmq.SUBSCRIBE, f"PUB {topic}")
else:
    print("Opção inválida. Por favor, tente novamente.")

for i in range(5):
    message = s.recv()
    print(bytes.decode(message))


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
