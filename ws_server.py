import asyncio
import websockets
import pickle
import json
import socket

HOST = '192.168.50.32'  # The socket server's hostname or IP address
PORT = 65431        # The port used by the server
Gateway_IP = '127.0.0.1'  # for websocket server

data = ''
connect = 0

async def hello(websocket, path):
    while True:
        if connect != 0:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)
            line = await websocket.recv()
            print(data)
            if line is None:
                return
            await websocket.send(data)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()  
conn, addr = s.accept()
with conn:
    print('sdsdsd')
    connect = conn
    start_server = websockets.serve(hello, "127.0.0.1", 8866)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


            


