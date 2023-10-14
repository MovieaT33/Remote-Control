import requests


def receive_message(domen: str, data: dict[str, str], debug: bool = True) -> str:
    response = requests.get(f"{domen}/api/v0/receive_message", params=data)
    if debug:
        print("INFO:", response.status_code)
    return response.text
