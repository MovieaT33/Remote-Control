from typing import Dict
import requests


def get_file(domen: str, params: Dict[str, str]) -> str:
    response: requests.models.Response = requests.get(f"{domen}/api/v0/get_file", params=params)
    print(f"[HTTP] {response.status_code}")
    return response.text
