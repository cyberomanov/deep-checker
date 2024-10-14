import json

import requests
from loguru import logger

from datatypes.airdrop import ExplorerResponse
from tools.add_logger import add_logger
from tools.change_ip import execute_change_ip
from tools.other_utils import read_file, get_proxied_session
from user_data.config import mobile_proxy, change_ip_url


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


if __name__ == '__main__':
    add_logger(version='v1.0')
    try:
        addresses = read_file(path='user_data/address.txt')
        session = get_proxied_session(proxy=mobile_proxy)
        for index, address in enumerate(addresses, start=1):
            airdrop = get_deep_airdrop(index=index, address=address, session=session)
            if airdrop.result.data:
                logger.success(f"{index} | {address} | airdrop | eligible.")
            else:
                logger.info(f"{index} | {address} | airdrop | not eligible.")
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        logger.exception(e)
