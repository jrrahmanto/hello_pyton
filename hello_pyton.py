from flask import Flask, jsonify, request

app = Flask(__name__)

# Inisialisasi data dalam bentuk list
data = []

# Endpoint untuk mendapatkan data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Endpoint untuk menambahkan data
@app.route('/data', methods=['POST'])

def add_data():
    new_data = request.get_json()
    data.append(new_data)
    return jsonify({"message": "Data telah ditambahkan", "data": new_data})

if __name__ == '__main__':
    app.run(debug=True)