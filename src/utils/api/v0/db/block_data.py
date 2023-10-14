import requests


def block_data(domen: str, data: dict[str, str], debug: bool = True) -> str:
    response = requests.get(f"{domen}/api/v0/block_data", params=data)
    if debug:
        print("INFO:", response.status_code)
    return response.text
