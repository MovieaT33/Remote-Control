from typing import Callable, Iterable, Any
import threading


class Task(threading.Thread):
    def __init__(
        self, target: Callable[..., object] | None = None, args: Iterable[Any] = ()
    ) -> None:
        super().__init__()
        self.target = target
        self.args = args
        self.running: bool = False

    def run(self):
        self.running = True
        while self.running:
            self.target(*self.args)

    def stop(self) -> None:
        self.running = False
