import socket
from ast import literal_eval

# Klockcraft Java Edition 1.20 Server

print('Starting Server...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_configs = literal_eval(open('configs/server_configs.json', 'r').read())
world_configs = literal_eval(open('configs/world_configs.json', 'r').read())

host = socket.gethostname()
port = server_configs['port']
player_limit = server_configs['player_limit']
s.bind((host, port))
s.listen(player_limit)
print(f'Started Server! Hosting on {host}, the server port is {port}.')