import json


# https://stackoverflow.com/questions/2262333/is-there-a-built-in-or-more-pythonic-way-to-try-to-parse-a-string-to-an-integer
def intTryParse(value):
    try:
        int(value)
        return True
    except ValueError as e:
        return False


def calculate(request):
    request_args = request.args
    if not request_args:
        msg = "No arguments recieved"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if "x" not in request_args or "y" not in request_args:
        msg = "x and y value not supplied"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if "x" in request_args and "y" in request_args:
        try:
            intTryParse(request_args['x'])
            intTryParse(request_args['y'])
            x = int(request_args['x'])
            y = int(request_args['y'])
        except Exception as e:
            msg = (
                "Invalid parameters for calculation: "
                "params are not valid integers"
            )
            print(f"error: {e}")
            return f"Bad Request: {msg}", 400

    r = {
        'calculation': '',
        'answer': 0,
    }

    try:
        r['answer'] = x % y
        r['calculation'] = x, '%', y
    except Exception as e:
        print(f"error: {e}")
        return "", 500

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }
    output = json.dumps(r)

    return output, 200, headers
