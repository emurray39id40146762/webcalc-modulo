from flask import Flask, request
import main

app = Flask(__name__)


@app.route('/', methods=['GET'])
def wrapper():
    return main.calculate(request)


if __name__ == '__main__':
    app.run(debug=True)
