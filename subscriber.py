import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://" + HOST + ":" + PORT
s.connect(p)

while True:
    print("1. Receber mensagens individuais")
    print("2. Receber mensagens de um tópico")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        username = input("Digite o nome do seu usuário: ")
        topic = f"USER.{username}"
        s.setsockopt_string(zmq.SUBSCRIBE, topic)
        while True:
            message = s.recv_string()
            print(f"Mensagem individual recebida: {message}")
    elif choice == "2":
        topic = input("Digite o nome do tópico: ")
        topic = f"TOPIC.{topic}"
        s.setsockopt_string(zmq.SUBSCRIBE, topic)
        while True:
            message = s.recv_string()
            print(f"Mensagem de tópico recebida: {message}")
    else:
        print("Opção inválida. Tente novamente.")


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
