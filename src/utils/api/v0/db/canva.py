import requests


def canva(domen: str, data: dict[str, str], debug: bool = True) -> str:
    response = requests.get(f"{domen}/canva", params=data)
    if debug:
        print("INFO:", response.status_code)
    return response.text
