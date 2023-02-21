from events import NetMinimizeEvent, NetRecoverEvent, NetListEvent
from data import Application

import json
from datetime import datetime


def parse(data):
    parsed_data = json.loads(data)
    return {
        "minimize": minimize,
        "recover": recover,
        "list": list,
    }[parsed_data.pop("action")](parsed_data)

def minimize(message):
    return NetMinimizeEvent(
        app=Application(
            window_title=message["title"],
            window_id=message["window_id"],
            time=datetime.now()
        ),
        workspace=message["workspace_id"]
    )

def recover(message):
    return NetRecoverEvent(
        title=message["title"],
        workspace=message.get("workspace_id", None)
    )

def list(message):
    return NetListEvent(
        workspace=message.get("workspace_id", None)
    )

