#!/usr/bin/env -S python3 -u

"""
Squad Teamkill tracker for the Fear and Terror Squad servers
"""

import asyncio
import logging
import sys

from . import bot
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)


def setup_logging(*, debug_on_stdout=False) -> None:
    """
    Sets up multiple rotating log files with different sensitivities.
    INFO will also be sent to stdout.
    WARNING and above will also be sent to stderr.
    DEBUG will only be sent to stdout if debug_on_stdout is True.

    :param debug_on_stdout: Whether DEBUG should be logged on stdout
    """

    formatter = logging.Formatter(
        "[%(asctime)s][%(levelname)s][%(name)s][%(funcName)s] %(message)s")

    # multiple files with different sensitivities
    log_debug = RotatingFileHandler("debug.log", mode='a',
                                    maxBytes=1 * 1024 * 1024 * 1024,  # 1GB
                                    encoding="UTF-8", delay=False,
                                    backupCount=2)
    log_debug.setLevel(logging.DEBUG)
    log_debug.setFormatter(formatter)
    log_info = RotatingFileHandler("info.log", mode='a',
                                   maxBytes=1 * 1024 * 1024 * 1024,  # 1GB
                                   encoding="UTF-8", delay=False,
                                   backupCount=2)
    log_info.setLevel(logging.INFO)
    log_info.setFormatter(formatter)
    log_warning = RotatingFileHandler("warning.log", mode='a',
                                      maxBytes=1 * 1024 * 1024 * 1024,  # 1GB
                                      encoding="UTF-8", delay=False,
                                      backupCount=2)
    log_warning.setLevel(logging.WARNING)
    log_warning.setFormatter(formatter)

    stdout_level = logging.DEBUG if debug_on_stdout else logging.INFO
    log_stdout = logging.StreamHandler(stream=sys.stdout)
    log_stdout.setLevel(stdout_level)
    log_stdout.setFormatter(formatter)

    log_stderr = logging.StreamHandler(stream=sys.stderr)
    log_stderr.setLevel(logging.WARNING)
    log_stderr.setFormatter(formatter)

    # filter discord and websocket on stdout
    def filter_discord(record):
        return not (record.name.startswith("discord.")
                    or record.name.startswith("websockets."))

    # filter WARNING and above on stdout
    def filter_above_info(record):
        return record.levelno <= logging.INFO

    log_stdout.addFilter(filter_discord)
    log_stderr.addFilter(filter_discord)
    log_stdout.addFilter(filter_above_info)

    logging.basicConfig(level=logging.NOTSET,
                        handlers=[log_debug, log_info, log_warning, log_stdout,
                                  log_stderr])

    global logger
    logger = logging.getLogger(__name__)


if __name__ == "__main__":
    setup_logging(debug_on_stdout=False)
    asyncio.run(bot.main())
