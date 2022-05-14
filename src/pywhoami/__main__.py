# SPDX-License-Identifier: MIT
# Copyright Contributors to the pywhoami project

import argparse
import asyncio
import os
from typing import List

import hypercorn
from .asgi import app


DEFAULT_PYWHOAMI_BIND = "127.0.0.1:8080"


parser = argparse.ArgumentParser(description="A Simple HTTP Request Analysis Server")
parser.add_argument(
    "-b",
    "--bind",
    action="store",
    help="Hostname/IP and port to run the server on. Defaults to 127.0.0.1:8080",
)
args = parser.parse_args()


def _serve() -> None:
    """
    Start the  pywhoami server
    """
    hypercorn_config = hypercorn.Config()
    hypercorn_config.bind = _get_bind()
    asyncio.run(hypercorn.asyncio.serve(app, hypercorn_config))


def _get_bind() -> List[str]:
    """
    Get the hostname and port binding

    Returns:
        str: ex: 127.0.0.1:8080
    """
    bind = DEFAULT_PYWHOAMI_BIND
    if env_bind := os.environ.get("PYWHOAMI_BIND"):
        bind = env_bind

    if args.bind:
        bind = args.bind
    return [bind]


if __name__ == "__main__":
    _serve()
