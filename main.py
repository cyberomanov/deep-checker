from loguru import logger

from tools.add_logger import add_logger
from tools.explorer import get_wrapper_airdrop
from tools.other_utils import read_file, get_proxied_session
from user_data.config import mobile_proxy

if __name__ == '__main__':
    add_logger(version='v1.0')
    try:
        addresses = read_file(path='user_data/address.txt')
        session = get_proxied_session(proxy=mobile_proxy)
        for index, address in enumerate(addresses, start=1):
            try:
                airdrop = get_wrapper_airdrop(index=index, address=address, session=session)
                if airdrop.result.data:
                    logger.success(f"{index} | {address}: eligible.")
                else:
                    logger.info(f"{index} | {address}: not eligible.")
            except Exception as e:
                logger.exception(e)
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        logger.exception(e)
