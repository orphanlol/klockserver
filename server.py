import socket
from ast import literal_eval

# Klockcraft Java Edition 1.20 Server

print('[STARTING] Starting Server...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_configs = literal_eval(open('configs/server_configs.json', 'r').read())
world_configs = literal_eval(open('configs/world_configs.json', 'r').read())

host = socket.gethostname()
port = server_configs['port']
player_limit = server_configs['player_limit']
online_mode = server_configs['online_mode']

if online_mode == 'true': online_mode = True
else: online_mode = False

s.bind((host, port))
s.listen(player_limit)
print(f'[STARTED] Started Server! Hosting on {host}, the server port is {port}.')

players_online = 0


while True:
    clientsocket, address = s.accept()

    # check if the player is connecting from the same computer as the server for online mode
    if online_mode:
        pass
    else:
        if list(address)[0] != socket.gethostbyname(socket.gethostname()): clientsocket.close()
    