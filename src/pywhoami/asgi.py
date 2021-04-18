"""
pywhoami. A Simple HTTP Request Analysis Server.
Copyright (C) 2020  Tom Saunders

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses
"""

import json
import pprint
import socket

from quart import Quart, request, make_response, Response

app = Quart("whoami")


@app.route("/", methods=["GET", "POST", "PATCH", "PUT", "DELETE"])
async def index() -> Response:
    """
    Receive details information about the HTTP request as plain text.
    """
    # TODO: Add "wait" query arg handling
    hostname = f"Hostname: {socket.gethostname()}"

    net_interfaces = {i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)}
    ips = [f"IP: {ip}" for ip in net_interfaces]
    remote_address = f"RemoteAddr: {request.remote_addr}"

    full_path = request.full_path
    if full_path == "/?":
        full_path = "/"
    access_log = (
        f"{request.method} {full_path} "
        + f"{request.scope['scheme'].upper()}/{request.scope['http_version']}"
    )

    host = f"Host: {request.host}"

    user_agent = f"User-Agent: {request.user_agent}"

    sorted_headers = sorted(request.headers.items(), key=lambda x: x[0])
    headers = []
    for key, value in sorted_headers:
        if key not in ("User-Agent", "Host"):
            headers.append(f"{key}: {value}")

    args = list(request.args.to_dict(flat=False).items())
    if len(args) == 0:
        query_args = []
    else:
        query_args = ["\nSearch"]
        for arg in args:
            for repeat in arg[1]:
                query_args.append(f"{arg[0]}: {repeat}")

    if body := await request.json:
        body = [pprint.pformat(body)]
    elif body := await request.form:
        body_dict = body.to_dict(flat=False)
        body = []
        for key, value in body_dict.items():
            for item in value:
                body.append(f"{key}: {item}")
    elif body := await request.get_data():
        body = [body.decode()]
    else:
        body = []

    if body:
        body.insert(0, "\nBody")

    responseData = "\n".join(
        [
            hostname,
            *ips,
            remote_address,
            access_log,
            host,
            user_agent,
            *headers,
            *query_args,
            *body,
        ]
    )

    response = await make_response(responseData, 200)
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    return response


@app.route("/api", methods=["GET", "POST", "PATCH", "PUT", "DELETE"])
async def api() -> Response:
    """
    Echo request data as JSON
    """
    hostname = socket.gethostname()

    net_interfaces = {i[4][0] for i in socket.getaddrinfo(hostname, None)}
    ips = [ip for ip in net_interfaces]

    headers = {}
    for key, value in sorted(request.headers.items(), key=lambda x: x[0]):
        if key not in ("User-Agent", "Host"):
            headers[key] = value
    if not headers:
        headers = None

    search = request.args.to_dict(flat=False) or None

    body = (
        await request.json
        or (await request.form).to_dict(flat=False)
        or (await request.get_data()).decode()
        or None
    )

    responseData = {
        "hostname": hostname,
        "ips": ips,
        "remoteAddr": request.remote_addr,
        "method": request.method,
        "url": request.full_path,
        "protocol": (
            f"{request.scope['scheme'].upper()}/" + request.scope["http_version"]
        ),
        "host": request.host,
        "userAgent": str(request.user_agent),
        "headers": headers,
        "search": search,
        "body": body,
    }

    response = await make_response(json.dumps(responseData, sort_keys=False), 200)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


@app.route("/bench", methods=["GET", "POST", "PATCH", "PUT", "DELETE"])
async def bench() -> Response:
    """
    Returns 1
    """
    response = await make_response("1", 200)
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    return response


@app.route("/data", methods=["GET", "POST", "PATCH", "PUT", "DELETE"])
async def data() -> Response:
    """
    Reply's with a response of the chosen size.
    """
    return await make_response("Not Found", 404)


@app.route("/echo")
async def echo() -> Response:
    """
    Echo for Websockets
    """
    return await make_response("Not Found", 404)


@app.route("/health", methods=["GET", "POST"])
async def health() -> Response:
    """
    Health check endpoint
    """
    return await make_response("Not Found", 404)
