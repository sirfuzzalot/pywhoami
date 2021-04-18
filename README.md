<div align="center">

<img src="./images/pywhoami-logo.jpg" width="60%" alt="pywhoami logo" />

# A Simple HTTP Request Analysis Server

[![PyPI Version](https://img.shields.io/pypi/v/pywhoami.svg)](https://pypi.python.org/pypi/pywhoami)
[![Docs](https://img.shields.io/badge/docs-passing-brightgreen.svg)](https://github.com/sirfuzzalot/pywhoami)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Versions](https://shields.io/pypi/pyversions/pywhoami)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

Pywhoami is inspired by the [whoami](https://github.com/containous/whoami)
Go server by [Traefik Labs](https://traefik.io/). Send a request to one
of the endpoints to get back details from your HTTP request. With
**pywhoami** you can help answer questions like, what headers were added
to my original request by a proxy server.

- [Using the PyPI Package](#using-the-pypi-package)
- [Using the Docker Image](#using-the-docker-image)
- [HTTP API Reference](#using-the-http-api)
- [Contributing](#contributing)

---

## Using the PyPI Package

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

### Customization

**pywhoami** allows you to customize the host and port that it runs on.
It determines the final results in this order, with the last one winning:

```
Defaults -> Environment Variables -> Command Line Args
```

#### bind

Customize the host and port that **pywhoami** runs on.

|     Default      |    ENV VAR    |    CLI     |
| :--------------: | :-----------: | :--------: |
| "127.0.0.1:8080" | PYWHOAMI_BIND | -b, --bind |

bash

```bash
# ENV VAR
export PYWHOAMI_BIND=0.0.0.0:5000
python3 -m pywhoami

# CLI
python3 -m pywhoami --bind 0.0.0.0:5000
```

powershell

```powershell
# ENV VAR
$env:PYWHOAMI_BIND="0.0.0.0:5000"
py -m pywhoami

# CLI
py -m pywhoami --bind 0.0.0.0:5000
```

---

### Using Docker

You will need the following:

- Git
- Docker Engine (Linux) or Docker Desktop (MacOS or Windows)

Clone the project.

```bash
git clone https://github.com/tomsaunders/pywhoami
```

Build the container image.

```
# cd to the git project root
cd pywhoami
docker build -t pywhoami .
```

Run **pywhoami** on your chosen port.

```bash
docker container run -p [your chosen port]:8080 pywhoami
```

Send it a test HTTP request.

```bash
>>> curl http://localhost:[your chosen port]/
Hostname: 1d12c578bd1a
IP: 172.19.0.2
RemoteAddr: 172.19.0.1
GET / HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.58.0
Accept: */*
```

---

## HTTP API Reference

- [/](#index)
- [/api](#api)

### index

Returns data about the HTTP request and OS.

#### Request

|           Method(s)           | Content-Type | Endpoint |
| :---------------------------: | :----------: | :------: |
| GET, POST, PATCH, PUT, DELETE |     ANY      |    /     |

No Query Args

#### Response

| Status | Content-Type |
| :----: | :----------: |
|  200   |  text/plain  |

```bash
>>>curl -H "Content-Type: application/x-www-form-urlencoded" \
... -d "user=13f3sf3sg&email=example%40example.com" http://localhost:8080
Hostname: 1d14c508bf1a
IP: 172.19.0.2
RemoteAddr: 172.19.0.1
POST / HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.58.0
Accept: */*
Content-Length: 42
Content-Type: application/x-www-form-urlencoded

Body
user: 13f3sf3sg
email: example@example.com
```

### /api

Returns the same data as `/`, but formatted as `application/json`.

#### Request

|           Method(s)           | Content-Type | Endpoint |
| :---------------------------: | :----------: | :------: |
| GET, POST, PATCH, PUT, DELETE |     ANY      |   /api   |

No Query Args

#### Response

| Status |   Content-Type   |
| :----: | :--------------: |
|  200   | application/json |

```bash
>>>curl -H "Content-Type: application/x-www-form-urlencoded" \
... -d "user=13f3sf3sg&email=example%40example.com" http://localhost:8080/api
{
  "hostname":"1d14c508bf1a",
  "ips":[
    "172.19.0.2"
  ],
  "remoteAddr":"172.19.0.1",
  "method":"POST",
  "url":"/api?",
  "protocol":"HTTP/1.1",
  "host":"localhost:8080",
  "userAgent":"curl/7.58.0",
  "headers":{
    "Accept":"*/*",
    "Content-Length":"42",
    "Content-Type":"application/x-www-form-urlencoded"
  },
  "search":null,
  "body":{
    "user":[
      "13f3sf3sg"
    ],
    "email":[
      "example@example.com"
    ]
  }
}
```

---

## Contributing

### Setting up the Development Environment

You will need to the following:

- [Git](https://git-scm.com/downloads) - distributed version control system
- [Docker Desktop](https://www.docker.com/products/docker-desktop) or [Docker Engine](https://hub.docker.com/search?q=&type=edition&offering=community&operating_system=linux) - container development system

1. Clone the project.

   ```bash
   git clone https://github.com/tomsaunders/pywhoami
   ```

2. Create a `.env` file from the template.

   bash

   ```bash
   cd ./pywhoami
   cp ./tools/dotenv_template.env ./.env
   ```

   powershell

   ```powershell
   cd .\pywhoami
   Copy-Item .\tools\dotenv_template.env -Destination .\.env
   ```

3. Start the development server.

   By default the **pywhoami** dev
   server is available on http://localhost:8080/. You can customize the
   port by specifying the **PYPORT** env variable in the `.env` file.

   ```bash
   cd pywhoami
   docker-compose up
   ```

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

### PyPI Package Development

To work on **pywhoami** as used in the PyPI package you will want to do
the following.

1. Create a virtual environment

   bash

   ```bash
   cd pywhoami
   python3 -m venv venv
   source venv/bin/activate
   ```

   powershell

   ```powershell
   cd pywhoami
   py -m venv venv
   .\venv\Scripts\activate
   ```

2. Install the **pywhoami** package in editable mode.

   ```bash
   pip install -e .
   ```

3. Run the server. Note that it is not setup for reloading.

   ```bash
   python -m pywhoami
   ```

### Publishing to PyPI

Instructions for a manual deployment to PyPI.

1. In your virtual environment install the build tools

   ```bash
   pip install --upgrade build twine
   ```

2. Ensure the version number is properly incremented.

   ```ini
   # setup.cfg
   [metadata]
   name = pywhoami
   version = 1.0.1
   ```

3. Build the distribution

   ```bash
   python -m build
   ```

4. Setup a credentials file (Optional)

   ```ini
   # [user home directory]/.pypirc
   [testpypi]
   username = __token__
   password = <my API token>
   ```

5. Publish it (note you can test publishes by using TestPyPi)

   ```bash
   twine upload dist/*

   # For Test PyPI
   twine upload --repository testpypi dist/*
   ```

6. Download and Verify the publish.

   ```bash
   pip install pywhoami

   # For Test PyPI. No deps is safer, though you can only verify package contents
   pip install --index-url https://test.pypi.org/simple/ --no-deps pywhoami
   ```

   ```bash
   python -m pywhoami
   ```

### Roadmap

Some possible features on the roadmap.

- Support for TLS
- Support for naming the server
- /data?size=n[&unit=u]
- /echo
- /health
- /?wait=d
- GitHub Actions build container image
- GitHub Action build and deploy package to pypi
- Support for validating webhooks
- Web UI for viewing request data as an alternative to viewing it in
  the HTTP response
