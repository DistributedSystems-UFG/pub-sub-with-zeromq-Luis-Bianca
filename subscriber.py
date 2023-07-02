import zmq
import time
from constPS import *

context = zmq.Context()
pub_socket = context.socket(zmq.PUB)
pub_socket.bind(f"tcp://{HOST}:{PUB_PORT}")

rpc_socket = context.socket(zmq.REP)
rpc_socket.bind(f"tcp://{HOST}:{RPC_PORT}")

while True:
    print("1. Enviar mensagem individual (RPC)")
    print("2. Enviar mensagem para tópico (Pub-Sub)")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        username = input("Digite o nome do usuário destinatário: ")
        message = input("Digite a mensagem: ")
        topic = f"USER.{username}"
        msg = f"{topic} {message}"
        rpc_socket.send_string(msg)
        response = rpc_socket.recv_string()
        print("Resposta do servidor (RPC):", response)
    elif choice == "2":
        topic = input("Digite o nome do tópico: ")
        message = input("Digite a mensagem: ")
        topic = f"TOPIC.{topic}"
        msg = f"{topic} {message}"
        pub_socket.send_string(msg)
    else:
        print("Opção inválida. Tente novamente.")

    time.sleep(2)


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
