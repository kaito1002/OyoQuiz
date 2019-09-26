from wsgiref.simple_server import make_server
import json

key = ''
port = 55544


def webhook(environ, start_response):
    print('Get Request!')
    headers = [
        ('Content-type', 'application/json; charset=utf-8'),
        ('Access-Control-Allow-Origin', '*'),
    ]

    start_response(f"200 OK", headers)

    return [json.dumps(
        {'message': "OK"}
    ).encode("utf-8")]


httpd = make_server('', port, webhook)
print(f"Serving on port {port}...")
httpd.serve_forever()
