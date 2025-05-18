from helper.logger_helper import logger


def clear_file(path: str):
    open(path, "w").close()
    logger.info(f"Cleared file content: {path}")