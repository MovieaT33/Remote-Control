import requests


def get_db(domen: str, data: dict[str, str], debug: bool = True) -> str:
    response = requests.get(f"{domen}/api/v0/get_file", params=data)
    if debug:
        print("INFO:", response.status_code)
    return response.text
