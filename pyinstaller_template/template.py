import logging

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def say_hello(name: str) -> str:
    logger.info(f"name is {name}")
    print(f"Hello {name}!")
    return

