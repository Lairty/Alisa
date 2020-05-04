import logging

logging.basicConfig(
    filename='log.log',
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)


def add_to_log(level, text):
    if level == "Debug":
        logging.debug(text)
    elif level == "Info":
        logging.info(text)
    elif level == "Warning":
        logging.warning(text)
    elif level == "Error":
        logging.error(text)
    elif level == "Critical":
        logging.critical(text)
