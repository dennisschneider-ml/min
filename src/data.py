from dataclasses import dataclass
from datetime import datetime


@dataclass
class Application:

    window_id: int
    window_title: str
    time: datetime

    def to_tuple(self):
        return (self.window_id, self.window_title)

