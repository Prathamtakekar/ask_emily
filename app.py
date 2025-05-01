# app.py
from flask import Flask, request, render_template, jsonify
from bridge_data import fetch_bridge_data
from gps_routing import get_route
from technician_finder import find_technicians
from chatbot import chatbot_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/bridge_data', methods=['GET'])
def bridge_data():
    data = fetch_bridge_data()
    return render_template('bridge_data.html', data=data) if data else "No bridge data available."

@app.route('/api/route', methods=['POST'])
def route():
    start = request.form['start']
    end = request.form['end']
    directions = get_route(start, end)
    return render_template('route.html', directions=directions) if directions else "Route not found."

@app.route('/api/find_technician', methods=['POST'])
def find_technician():
    location = request.form['location']
    service = request.form['service']
    techs = find_technicians(location, service)
    return jsonify(techs)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot_query(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
