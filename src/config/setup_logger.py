import logging


def setup_logger():
    """
    Initializes the logger for the project.
    Sets the logging level and format.
    """

    LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        level=logging.INFO,  # Show INFO and above by default
        format=LOG_FORMAT,
        datefmt=DATE_FORMAT,
    )

    # Create your project-specific logger
    return logging.getLogger("aviationstack.fetcher")
