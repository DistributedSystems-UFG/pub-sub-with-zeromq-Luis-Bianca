import zmq
import time
from constPS import *

context = zmq.Context()
s = context.socket(zmq.PUB)
p = "tcp://" + HOST + ":" + PORT
s.bind(p)

while True:
    print("Escolha uma opção:")
    print("1. Enviar mensagem individual")
    print("2. Enviar mensagem para tópico")
    print("3. Sair")
    option = input("Opção: ")

    if option == "1":
        recipient = input("Digite o nome do destinatário: ")
        message = input("Digite a mensagem: ")
        msg = str.encode(f"RPC {recipient} {message}")
        s.send(msg)
    elif option == "2":
        topic = input("Digite o tópico: ")
        message = input("Digite a mensagem: ")
        msg = str.encode(f"PUB {topic} {message}")
        s.send(msg)
    elif option == "3":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")

#import zmq, time
#from constPS import * #-

#context = zmq.Context()
#s = context.socket(zmq.PUB)        # create a publisher socket
#p = "tcp://"+ HOST +":"+ PORT      # how and where to communicate
#s.bind(p)                          # bind socket to the address
#while True:
#	time.sleep(5)                    # wait every 5 seconds
#	msg = str.encode("TIME " + time.asctime())
#	s.send(msg) # publish the current time
#
