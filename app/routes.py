from flask import jsonify, request
from app import app, db
from app.models import Item
from app.schemas import item_schema, items_schema


@app.route('/')
def hello_world():
    return "Hello World!!!!!!!!!!!!!"

@app.route('/create-item', methods=['POST'])
def create_new_item():
    item = request.json['item']
    completed = False
    db.session.add(item, completed)
    db.session.commit()
    return item.schema.jsonify(item)

@app.route('/item/all', methods=['GET'])
def get_all_items():
    all_items = Item.query.all()
    return jsonify(items_schema.dump(all_items))