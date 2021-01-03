<div align="center">

<img src="./images/pywhoami-logo.jpg" width="60%" alt="pywhoami logo" />

# A Simple HTTP Request Analysis Server

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

</div>

Pywhoami is inspired by the [whoami](https://github.com/containous/whoami)
Go server by [Traefik Labs](https://traefik.io/). Send a request to one
of the endpoints to get back details from your HTTP request. With
**pywhoami** you can help answer questions like, what headers were added
to my original request by a proxy server.

- [Quick Start](#quick-start)
- [Using the HTTP API](#using-the-http-api)
- [Contributing](#contributing)
- [License](./LICENSE)

## Quick Start

To deploy **pywhoami** we recommend using Docker. The next phase of this
project will add pypi package support, but for now Docker.

You will need the following:

- Git
- Docker Engine (Linux) or Docker Desktop (MacOS or Windows)

Clone the project.

```bash
git clone https://github.com/tomsaunders/pywhoami
```

Build the container image.

```
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

## Using the HTTP API

- [/](#index)
- [/api](#api)

## index

Returns data about the HTTP request and OS.

## Request

|           Method(s)           | Content-Type | Endpoint |
| :---------------------------: | :----------: | :------: |
| GET, POST, PATCH, PUT, DELETE |     ANY      |    /     |

No Query Args

## Response

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

## /api

Returns the same data as `/`, but formatted as `application/json`.

## Request

|           Method(s)           | Content-Type | Endpoint |
| :---------------------------: | :----------: | :------: |
| GET, POST, PATCH, PUT, DELETE |     ANY      |   /api   |

No Query Args

## Response

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

## Contributing

### Setting up the Development Environment

You will need to the following:

- [Git](https://git-scm.com/downloads) - distributed version control system
- [Docker Desktop](https://www.docker.com/products/docker-desktop) or [Docker Engine](https://hub.docker.com/search?q=&type=edition&offering=community&operating_system=linux) - container development system

Clone the project.

```bash
git clone https://github.com/tomsaunders/pywhoami
```

Create a `.env` file from the template.

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

Start the development server. By default the **pywhoami** dev
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

### Roadmap

- Support for TLS
- Support for custom port
- Support for naming the server
- /data?size=n[&unit=u]
- /echo
- /health
- /?wait=d
- pypi package
- GitHub Actions build container image
- GitHub Action build and deploy package to pypi
