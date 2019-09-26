#!/usr/bin/python3
from wsgiref.simple_server import make_server
import subprocess
import json
import threading

KEY = ''


def deploy():
    subprocess.run(
        ['sudo', 'bash', '/home/ubuntu/deploy.sh'],
        cwd="/home/ubuntu"
        )


def webhook(environ, start_response):
    print('Get Request!')
    status = '200'
    headers = [
        ('Content-type', 'application/json; charset=utf-8'),
        ('Access-Control-Allow-Origin', '*'),
    ]
    message = ""
    is_fail = False
    try:
        content_length = environ.get('CONTENT_LENGTH', 0)
        body = environ.get('wsgi.input').read(int(content_length)).decode()
        data = json.loads(body)
    except Exception as e:
        is_fail = True
        message = str(e)
        data = {'key': ''}
        print(e)

    if not is_fail and data['key'] == KEY:
        # auth
        message = "OK"
        print("Authorized.")
        deploy_thread = threading.Thread(target=deploy)
        deploy_thread.start()
    else:
        message = f"Fail\n{message}"
        print("Failed.")
    start_response(f"{status} {message}", headers)
    return [json.dumps(
        {'message': message}
    ).encode("utf-8")]


httpd = make_server('', 55544, webhook)
print("Serving on port 55544...")
httpd.serve_forever()
