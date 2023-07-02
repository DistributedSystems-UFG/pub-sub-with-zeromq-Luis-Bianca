import zmq
from constPS import *

context = zmq.Context()
sub_socket = context.socket(zmq.SUB)
sub_socket.connect(f"tcp://{HOST}:{PUB_PORT}")
sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")

rpc_socket = context.socket(zmq.REQ)
rpc_socket.connect(f"tcp://{HOST}:{RPC_PORT}")

while True:
    print("1. Receber mensagens individuais (RPC)")
    print("2. Receber mensagens de um tópico (Pub-Sub)")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        username = input("Digite o nome do seu usuário: ")
        topic = f"USER.{username}"
        message = input("Digite a mensagem: ")
        msg = f"{topic} {message}"
        rpc_socket.send_string(msg)
        response = rpc_socket.recv_string()
        print("Resposta do servidor (RPC):", response)
    elif choice == "2":
        topic = input("Digite o nome do tópico: ")
        topic = f"TOPIC.{topic}"
        while True:
            message = sub_socket.recv_string()
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
