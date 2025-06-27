# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

menu = []

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu), 200

@app.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.get_json()
    item = {
        "name": data["name"],
        "price": data["price"],
        "availability": data["availability"]
    }
    menu.append(item)
    return jsonify({"message": "Item added", "item": item}), 201

@app.route('/menu/<string:name>', methods=['DELETE'])
def delete_item(name):
    global menu
    menu = [item for item in menu if item["name"].lower() != name.lower()]
    return jsonify({"message": f"{name} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
