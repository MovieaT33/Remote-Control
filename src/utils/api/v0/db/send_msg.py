from typing import Dict
import requests


def send_msg: str, params: Dict[str, str]) -> str:
    response: requests.models.Response = requests.get(f"{domen}/api/v0/send_msg", params=params)
    print(f"[HTTP] {response.status_code}")
    return response.text
