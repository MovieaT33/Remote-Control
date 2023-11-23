from typing import Dict
import requests


def block_info(domen: str, params: Dict[str, str]) -> str:
    response: requests.models.Response = requests.get(f"{domen}/api/v0/block_info", params=params)
    print(f"[HTTP] {response.status_code}")
    return response.text
