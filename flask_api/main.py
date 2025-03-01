from flask import Flask, jsonify, render_template, request, abort

app = Flask(__name__)

# Sample data
items = [
    {'id': 1, 'name': 'Laptop', 'price': 1200},
    {'id': 2, 'name': 'Mouse', 'price': 25},
    {'id': 3, 'name': 'Keyboard', 'price': 75}
]

# Welcome message in JSON format
@app.route('/')
def welcome():
    return jsonify({'message': 'Welcome to the Flask API!'})

# List of items in JSON format
@app.route('/items', methods=['GET', 'POST'])
def list_items():
    if request.method == 'GET':
        return jsonify(items)
    elif request.method == 'POST':
        new_item = {
            'id': len(items) + 1,
            'name': request.form['name'],
            'price': float(request.form['price'])  # Convert price to float
        }
        items.append(new_item)  # Append new item to the global items list
        return jsonify(new_item), 201  # Created

# Details of a specific item by ID
@app.route('/items/<int:item_id>')
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        abort(404)  # Not Found

#Handle 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Item not found'}), 404

# Jinja2 template to display items
@app.route('/items_web')
def list_items_web():
    return render_template('items.html', items=items)  # Pass the updated 'items' list to the template

# Display add new item form using Jinja2
@app.route('/add_item_web', methods=['GET', 'POST'])
def add_item_web():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])  # Convert the price into float

        # Create a new item and add it to the items list
        new_item = {
            'id': len(items) + 1,
            'name': name,
            'price': price
        }
        items.append(new_item)

        return render_template('form_result.html', name=name, price=price)
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(debug=True)
