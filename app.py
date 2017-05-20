from flask import Flask, abort,jsonify
from services import Services

app = Flask(__name__)
services = Services()


@app.route('/')
def index():
    return "Welcome to Open Calander!"

@app.route('/calander/api/v0.0/calanders', methods=['GET'])
def get_calanders():
    return jsonify({'calanders': [services.public_calander(services.getcalanders()) for calander in services.public_calander(services.getcalanders())]})

@app.route('/calander/api/v0.0/calanders/<int:cal_id>', methods=['GET'])
def get_calander(cal_id):
    cal_data = services.getcalanders()
    calander = [calander for calander in cal_data if calander['cal_id'] == cal_id ]
    if len(calander) == 0:
        abort(404)
    return jsonify({'calander': calander[0]})

if __name__ == '__main__':
    app.run(debug=True)

