registrar = []

def register(event_handler):
    registrar.append(event_handler)

def broadcast(event):
    for event_handler in registrar:
        event_handler.receive(event)


class EventHandler:

    def receive(self, event):
        pass

