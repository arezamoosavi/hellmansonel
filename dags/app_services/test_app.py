import logging, os, sys
from pprint import pprint

logging.info("Starting logger for test app")
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


def print_context(data_path, **kwargs):
    """Print the Airflow context and ds variable from the context."""
    logger.info("DATA PATH: " + data_path)
    pprint(kwargs)
    logger.info("THIS APP IS DONE")
    return "Whatever you return gets printed in the logs"
