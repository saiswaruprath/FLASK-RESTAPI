from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the planetary API!!!')



@app.route('/not_found')
def not_found():
    return jsonify(message='sorry no data found'), 404.             ###adding 404 status code to show in postman once we trigger not found endpoint

if __name__ == '__main__':
    app.run()
