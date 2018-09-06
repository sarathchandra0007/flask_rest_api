from flask import Flask, jsonify

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
    return "hello,world!"

# POST Store data
@app.route('/store',methods=['POST'])
def create_store():
    pass

# GET store data
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET all stores data
@app.route('/store')
def get_stores():
    pass

#POST item
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    pass
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

app.run()
