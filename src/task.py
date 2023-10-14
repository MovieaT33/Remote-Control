from typing import Callable, Iterable, Any
import threading


class Task:
    def __init__(
        self, target: Callable[..., object] | None = None, args: Iterable[Any] = ()
    ) -> None:
        self.target = target
        self.args = args
        self.running: bool = False
        self.task: threading.Thread = threading.Thread(target=self.run)

    def start(self) -> None:
        self.target(*self.args)

    def run(self):
        self.running = True
        while self.running:
            self.start()

    def stop(self) -> None:
        self.running = False
