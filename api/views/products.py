from flask import jsonify, request, json
from api.views import shauri_blueprint
from api.models.database import db_connection
from api.models.models_1 import Products
from api.models.validators import is_valid_price
from flask_jwt_extended import jwt_required,get_jwt_identity
import datetime
from api.utils import image_1

@shauri_blueprint.route('/products', methods=['POST'])
@jwt_required
def create_product():
    user_identiy = get_jwt_identity()
    product_input = request.json
    if is_valid_price(product_input):
        return is_valid_price(product_input)
    product_name = request.json.get('product_name')
    price = request.json.get('price')
    new_product = Products(product_name,price,image_1,user_identiy['user_id'])
    db_connection.add_product(new_product)
    product = db_connection.query_last_item()
    return jsonify({"message":"product added successfully","product":product}),201
