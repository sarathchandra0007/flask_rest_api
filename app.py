from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name':'my_store',
        'items':[
            {
                'item' : 'my_item',
                'price' : 17.50
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST Store data
@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET store data
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : 'Store not found'})


#GET all stores data
@app.route('/store')
def get_stores():
    return jsonify({'stores' : stores})    # jsonify convert dict to json

#POST item
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            new_item = {
                'item' : request_data['item'],
                'price' : request_data['price']
                }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'Store not found'})




#GET item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'items not found'})

app.run()
