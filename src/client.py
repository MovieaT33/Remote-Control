import utils.api.v0.db as db
import datetime
import time
import json
import sys
from task import Task
from settings import DOMEN, DATA


def get_last_message(delay: float) -> str:
    print("Task initialization...")
    database = db.get_file(DOMEN, {**DATA})
    print(datetime.datetime.now())
    print("Task starting...")

    while True:
        time.sleep(delay)
        new_db_original = db.get_file(DOMEN, {**DATA})
        print(datetime.datetime.now())
        if database != new_db_original:
            new_db = new_db_original.splitlines()
            new_db = new_db[len(new_db) - 1]
            message = json.loads(new_db)["msg"]
            print("Last command (must be server message):", end=" ")
            print(f"\033[34m[\033[0m{message}\033[34m]\033[0m")
            database = new_db_original
            print(datetime.datetime.now())


def main(delay: float) -> None:
    print("Creating task...")
    get_message_task = Task(target=get_last_message, args=[delay,
                                                           debug])
    get_message_task.start()

    run = True
    while run:
        try:
            message = input("\033[32m>\033[0m: ")
            db.send_msg(DOMEN, {**DATA, "msg": message})
        except KeyboardInterrupt:
            get_message_task.stop()
            sys.exit()


if __name__ == "__main__":
    debug_question = input("Do you want enable debug [y/N]?")
    true_list = ("true", "yes", "y", "1")
    if debug_question.lower() in true_list:
        debug = True
    else:
        debug = False

    if input("Do you want to set delay [y/N]?").lower() in true_list:
        delay = float(input("Delay (in seconds): "))
    else:
        delay = 1.0

    main(delay, debug)
