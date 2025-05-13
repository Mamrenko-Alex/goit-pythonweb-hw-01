import logging


def get_logger(name: str, file_name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    print(f"Logger {name} initialized.")
    print(f"Log file: {file_name}")

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    fh = logging.FileHandler(file_name)
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
