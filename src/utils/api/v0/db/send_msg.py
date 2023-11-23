import requests


def receive_a_new_message(domen: str, data: dict[str, str], debug: bool = True) -> str:
    response = requests.get(f"{domen}/api/v0/send_msg", params=data)
    if debug:
        print("INFO:", response.status_code)
    return response.text
