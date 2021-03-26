import json
import os
import subprocess
import uuid

import requests
from requests.packages.urllib3.util.retry import Retry


def test_args_correct():
    name = str(uuid.uuid4())
    port = os.getenv('PORT', 8080)  # Each functions framework instance needs a unique port

    process = subprocess.Popen(
      [
        'functions-framework',
        '--target', 'calculate',
        '--port', str(port)
      ],
      cwd=os.path.dirname(__file__),
      stdout=subprocess.PIPE
    )

    # Send HTTP request simulating Pub/Sub message
    # (GCF translates Pub/Sub messages to HTTP requests internally)
    BASE_URL = f'http://localhost:{port}'

    retry_policy = Retry(total=6, backoff_factor=1)
    retry_adapter = requests.adapters.HTTPAdapter(
      max_retries=retry_policy)

    session = requests.Session()
    session.mount(BASE_URL, retry_adapter)

    name = str(uuid.uuid4())
    res = requests.get(
        '{}/calculate'.format(BASE_URL),
        params={'x': 10, 'y': 6}
    )
    r = {
        'calculation': '',
        'answer': 0,
    }
    x = 10
    y = 6
    answer = x % y
    r['answer'] = answer
    r['calculation'] = x, '%', y
    output = json.dumps(r)
    assert res.status_code == 200
    assert res.text == output

    # Stop the functions framework process
    process.kill()
    process.wait()


def test_args_x_str_y_int():
    name = str(uuid.uuid4())
    port = os.getenv('PORT', 8080)  # Each functions framework instance needs a unique port

    process = subprocess.Popen(
      [
        'functions-framework',
        '--target', 'calculate',
        '--port', str(port)
      ],
      cwd=os.path.dirname(__file__),
      stdout=subprocess.PIPE
    )

    # Send HTTP request simulating Pub/Sub message
    # (GCF translates Pub/Sub messages to HTTP requests internally)
    BASE_URL = f'http://localhost:{port}'

    retry_policy = Retry(total=6, backoff_factor=1)
    retry_adapter = requests.adapters.HTTPAdapter(
      max_retries=retry_policy)

    session = requests.Session()
    session.mount(BASE_URL, retry_adapter)

    name = str(uuid.uuid4())
    res = requests.get(
        '{}/calculate'.format(BASE_URL),
        params={'x': 'h', 'y': 6}
    )
    assert res.status_code == 400

    # Stop the functions framework process
    process.kill()
    process.wait()


def test_args_none():
    name = str(uuid.uuid4())
    port = os.getenv('PORT', 8080)  # Each functions framework instance needs a unique port

    process = subprocess.Popen(
      [
        'functions-framework',
        '--target', 'calculate',
        '--port', str(port)
      ],
      cwd=os.path.dirname(__file__),
      stdout=subprocess.PIPE
    )

    # Send HTTP request simulating Pub/Sub message
    # (GCF translates Pub/Sub messages to HTTP requests internally)
    BASE_URL = f'http://localhost:{port}'

    retry_policy = Retry(total=6, backoff_factor=1)
    retry_adapter = requests.adapters.HTTPAdapter(
      max_retries=retry_policy)

    session = requests.Session()
    session.mount(BASE_URL, retry_adapter)

    name = str(uuid.uuid4())
    res = requests.get(
        '{}/calculate'.format(BASE_URL),
        params={}
    )
    assert res.status_code == 400

    # Stop the functions framework process
    process.kill()
    process.wait()