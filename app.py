from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to simulate a pantry
pantry = {}

# Create (POST): Add a key-value pair to the Pantry
@app.route('/add-item', methods=['POST'])
def add_item():
    try:
        data = request.json  # Get data from request JSON
        pantry_id = data.get('pantry_id')
        basket_key = data.get('basket_key')
        value = data.get('value')

        if not pantry_id or not basket_key or not value:
            return jsonify({"error": "Invalid request data"}), 400

        if pantry_id not in pantry:
            pantry[pantry_id] = {}

        pantry[pantry_id][basket_key] = value
        return jsonify({"message": "Item added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Read (GET): Retrieve the value associated with a specified basket key
@app.route('/get-item/<string:pantry_id>/<string:basket_key>', methods=['GET'])
def get_item(pantry_id, basket_key):
    try:
        if pantry_id not in pantry or basket_key not in pantry[pantry_id]:
            return jsonify({"error": "Item not found"}), 404

        value = pantry[pantry_id][basket_key]
        return jsonify({"value": value}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# List Baskets (GET): List all baskets under a specified Pantry, optionally filtered by name
@app.route('/list-baskets/<string:pantry_id>', methods=['GET'])
def list_baskets(pantry_id):
    try:
        if pantry_id not in pantry:
            return jsonify({"error": "Pantry not found"}), 404

        name_filter = request.args.get('name_filter')
        baskets = pantry[pantry_id]

        if name_filter:
            filtered_baskets = {key: value for key, value in baskets.items() if name_filter in key}
            return jsonify(filtered_baskets), 200

        return jsonify(baskets), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update (PUT): Update the value associated with a specified basket key
@app.route('/update-item/<string:pantry_id>/<string:basket_key>', methods=['PUT'])
def update_item(pantry_id, basket_key):
    try:
        if pantry_id not in pantry or basket_key not in pantry[pantry_id]:
            return jsonify({"error": "Item not found"}), 404

        data = request.json
        new_value = data.get('value')

        if not new_value:
            return jsonify({"error": "Invalid request data"}), 400

        pantry[pantry_id][basket_key] = new_value
        return jsonify({"message": "Item updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete (DELETE): Delete a specific basket
@app.route('/delete-item/<string:pantry_id>/<string:basket_key>', methods=['DELETE'])
def delete_item(pantry_id, basket_key):
    try:
        if pantry_id not in pantry or basket_key not in pantry[pantry_id]:
            return jsonify({"error": "Item not found"}), 404

        del pantry[pantry_id][basket_key]
        return jsonify({"message": "Item deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200)
