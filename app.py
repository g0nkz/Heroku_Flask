from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from resources.user import UserRegister
from resources.item import Item, ItemList
from security import authenticate, identity
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dev'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')

if __name__ == "__main__":
    db.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)
