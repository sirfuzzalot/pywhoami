# SPDX-License-Identifier: MIT
# Copyright Contributors to the pywhoami project

import sys

from setuptools import setup

if sys.version_info < (3, 8, 0):
    sys.exit("Python 3.8.0+ Required")

long_description = """
# A Simple HTTP Request Analysis Server

[![PyPI Version](https://img.shields.io/pypi/v/pywhoami.svg)](https://pypi.python.org/pypi/pywhoami)
[![Docs](https://img.shields.io/badge/docs-passing-brightgreen.svg)](https://github.com/sirfuzzalot/pywhoami)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://shields.io/pypi/pyversions/pywhoami)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

Pywhoami is inspired by the [whoami](https://github.com/containous/whoami)
Go server by [Traefik Labs](https://traefik.io/). Send a request to one
of the endpoints to get back details from your HTTP request. With
**pywhoami** you can help answer questions like, what headers were added
to my original request by a proxy server.

Checkout the [documentation](https://github.com/sirfuzzalot/pywhoami).

---

## Quick Start

### Installation

bash

```bash
python3 -m pip install pywhoami
```

powershell

```powershell
py -m pip install pywhoami
```

### Running the Server

bash

```bash
>>> python3 -m pywhoami
[2021-04-17 15:00:25 -0700] [4400] [INFO] Running on http://127.0.0.1:8080 (CTRL + C to quit)
```

powershell

```powershell
>>> py -m pywhoami
[2021-04-17 15:00:25 -0700] [4400] [INFO] Running on http://127.0.0.1:8080 (CTRL + C to quit)
```

Send it a test HTTP request.

```bash
>>> curl http://localhost:8080/
Hostname: 1d12c578bd1a
IP: 172.19.0.2
RemoteAddr: 172.19.0.1
GET / HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.58.0
Accept: */*
```
"""

setup(
    long_description=long_description,
    long_description_content_type="text/markdown"
)
