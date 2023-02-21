from events import LogicListEvent, NetListEvent, NetMinimizeEvent, NetRecoverEvent, SendAckEvent
import broker


class Logic:

    def __init__(self) -> None:
        self.hidden_applications = {}

    def receive(self, event):
        if isinstance(event, NetMinimizeEvent):
            self.add(event.workspace, event.app)
            broker.broadcast(SendAckEvent())
        elif isinstance(event, NetRecoverEvent):
            self.remove(event.workspace, event.title)
            broker.broadcast(SendAckEvent())
        elif isinstance(event, NetListEvent):
            broker.broadcast(LogicListEvent(self.hidden_applications.get(event.workspace, [])))

    def add(self, workspace_id, app):
        old_hidden_apps = self.hidden_applications.get(workspace_id, [])
        self.hidden_applications[workspace_id] = old_hidden_apps+[app]
        print(self.hidden_applications[workspace_id])

    def remove(self, workspace_id, title):
        old_hidden_apps = self.hidden_applications.get(workspace_id, [])
        hidden_apps = [hidden_app for hidden_app in old_hidden_apps if title != hidden_app.window_title]
        self.hidden_applications[workspace_id] = hidden_apps
        print(self.hidden_applications[workspace_id])

    
