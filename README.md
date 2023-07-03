# Aplicação de Chat com ZeroMQ

Este é um conjunto de códigos que implementa uma aplicação de chat usando ZeroMQ. A aplicação suporta o envio de mensagens individuais através de RPC (Remote Procedure Call) e mensagens de tópicos usando o padrão pub-sub (Publish-Subscribe).

## Requisitos
Certifique-se de ter o ZeroMQ instalado em sua máquina antes de executar a aplicação. Você pode encontrar mais informações e instruções de instalação na documentação oficial do ZeroMQ <https://zeromq.org/languages/python/>.

## Como executar
1. Clone o repositório para sua máquina local.

2. Modifique constPS.py com o endereço IP e a porta corretos de acordo com a sua configuração.

3. Abra dois terminais ou janelas de comando separadas.

4. No primeiro terminal, execute o arquivo publisher.py:

5. No segundo terminal, execute o arquivo subscriber.py:

6. Siga as instruções exibidas no terminal para interagir com a aplicação de chat. Você poderá escolher entre enviar mensagens individuais ou mensagens para tópicos, e receber mensagens correspondentes no terminal do assinante.

## Arquivos
- publisher.py: Implementa o lado do publisher da aplicação de chat. Permite enviar mensagens individuais via RPC ou mensagens para tópicos usando o ZeroMQ.

- subscriber.py: Implementa o lado do subscriber da aplicação de chat. Permite receber mensagens individuais via RPC ou mensagens de tópicos usando o ZeroMQ.

- constPS.py: Arquivo de constantes contendo o endereço IP e a porta usados na comunicação entre o publisher e o subscriber.

## Observações
- Certifique-se de modificar o arquivo constPS.py com o endereço IP e a porta corretos de acordo com a sua configuração.

- Durante a execução do subscriber, você pode digitar "sair" a qualquer momento para desconectar do canal de mensagem ou tópico e voltar ao menu principal.

- Lembre-se de que a correta instalação e configuração do ZeroMQ é necessária para o funcionamento adequado desta aplicação.

## Alunos

Bianca Pereira de Carvalho - 202004706

Luís Guilherme Barbosa Custódio - 201905500
