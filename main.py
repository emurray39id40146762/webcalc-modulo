def calculate(request):
    x = 0
    y = 0
    r = {
        'error': False,
        'string': '',
        'answer': 0
    }
    request_json = request.get_json()
    try:
        x += request_json['x']
        y += request_json['y']
    except (TypeError, ValueError):
        r['error'] = True
        print("Both values have to be integers.")

    r['string'] = x, '%', y, '=', r['answer']
    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }
    if r['error']:
        return r, 400, headers
    else:
        return r, 200, headers
