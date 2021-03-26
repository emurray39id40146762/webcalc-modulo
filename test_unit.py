from unittest.mock import Mock
import json
from main import calculate


def test_print_answer():
    r = {
        'calculation': '',
        'answer': 0,
    }
    x = 10
    y = 6
    data = {'x': 10, 'y': 6}
    answer = x % y

    req = Mock(get_json=Mock(return_value=data), args=data)
    r['answer'] = answer
    r['calculation'] = x, '%', y
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }
    output = json.dumps(r)

    # Call tested function
    assert calculate(req) == (output, 200, headers)


def test_no_args():
    data = {}
    req = Mock(get_json=Mock(return_value=data), args=None)
    # Call tested function
    msg = "No arguments recieved"
    assert calculate(req) == (f"Bad Request: {msg}", 400)


def test_args_x_int_y_str():
    data = {'x': 10, 'y': 'j'}
    req = Mock(get_json=Mock(return_value=data), args=data)
    # Call tested function
    msg = (
        "Invalid parameters for calculation: "
        "params are not valid integers"
    )
    assert calculate(req) == (f"Bad Request: {msg}", 400)


def test_args_x_str_y_int():
    data = {'x': 'k', 'y': 7}
    req = Mock(get_json=Mock(return_value=data), args=data)
    # Call tested function
    msg = (
        "Invalid parameters for calculation: "
        "params are not valid integers"
    )
    assert calculate(req) == (f"Bad Request: {msg}", 400)
