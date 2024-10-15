import json

import requests
from loguru import logger

from datatypes.airdrop import ExplorerResponse
from tools.change_ip import execute_change_ip
from user_data.config import change_ip_url


def get_deep_airdrop(index: int, address: str, session: requests.Session()) -> ExplorerResponse:
    change_ip = execute_change_ip(change_ip_url=change_ip_url)
    if change_ip:
        logger.info(f"{index} | {address} | ip has been changed.")

    url = "https://fullnode.mainnet.sui.io/"
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "suix_getOwnedObjects",
        "params": [
            address, {
                "filter":
                    {"MatchAny":
                        [{
                            "StructType": "0xc2cfa18b841df1887d931055cf41f2773c58164f719675595d020829893188a5::distribution::DEEPAirdrop"
                        }]},
                "options":
                    {
                        "showType": True,
                        "showContent": True,
                        "showDisplay": True
                    }
            },
            None,
            50]
    }

    response = session.post(url=url, json=data)
    return ExplorerResponse.parse_obj(json.loads(response.content))


def get_wrapper_airdrop(index: int, address: str, session: requests.Session()) -> ExplorerResponse:
    change_ip = execute_change_ip(change_ip_url=change_ip_url)
    if change_ip:
        logger.info(f"{index} | {address} | ip has been changed.")

    url = "https://fullnode.mainnet.sui.io/"
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "suix_getOwnedObjects",
        "params": [
            address, {
                "filter":
                    {"MatchAny":
                        [{
                            "StructType": "0x61c9c39fd86185ad60d738d4e52bd08bda071d366acde07e07c3916a2d75a816::distribution::DEEPWrapper"
                        }]},
                "options":
                    {
                        "showType": True,
                        "showContent": True,
                        "showDisplay": True
                    }
            },
            None,
            50]
    }

    response = session.post(url=url, json=data)
    return ExplorerResponse.parse_obj(json.loads(response.content))
