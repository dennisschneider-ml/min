import broker
import events
import parsing
from logic import Logic

import os
import socket


class Network(broker.EventHandler):

    def __init__(self, socket_address):
        self.socket_address = socket_address
        try:
            os.unlink(socket_address)
        except OSError:
            if os.path.exists(socket_address):
                raise
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.connection = None

    def run(self):
        self._startup()
        self._run()

    def _startup(self):
        self.socket.bind(self.socket_address)
        self.socket.listen(1)

    def _run(self):
        while True:
            print("waiting ...")
            self.connection, _ = self.socket.accept()
            print("connected!")
            data = self.__receive_message(self.connection)
            print("received:", data)
            event = parsing.parse(data)
            print(event)

            broker.broadcast(event)

    def __receive_message(self, connection):
        data = connection.recv(1024).decode('utf-8')
        return data

    def _send(self, data):
        self.connection.sendall(data.encode('utf-8'))
    
    def close_connection(self):
        print("closed")
        self.connection.close()

    def receive(self, event):
        if isinstance(event, events.LogicListEvent):
            self._send('\n'.join([app.window_title+"\t"+\
                                     str(app.window_id)+"\t"+\
                                     app.time.strftime("%Y-%m-%d %H:%M:%S") for app in event.minimized]))
            self.close_connection()
        if isinstance(event, events.SendAckEvent):
            self.close_connection()
            
if __name__ == '__main__':
    logic = Logic()
    net = Network('./uds_socket')
    net.run()
