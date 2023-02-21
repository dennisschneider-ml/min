from dataclasses import dataclass
from data import Application


@dataclass
class NetMinimizeEvent:
    app: Application
    workspace: int

@dataclass
class NetRecoverEvent:
    title: str
    workspace: int

@dataclass
class NetListEvent:
    workspace: int

@dataclass
class LogicListEvent:
    minimized: list[Application]

@dataclass
class SendAckEvent:
    pass
