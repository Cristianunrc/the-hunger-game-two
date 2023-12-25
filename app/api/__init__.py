from flask import Blueprint
from flask_restful import Api

from app.api.user_resource import Register, SelectPj, UserGet, Login, UserIdGet, Logout
from app.api.game_resource import ConfigDistrict, Game

# Create a blueprint
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(ConfigDistrict, '/district')
api.add_resource(Game, '/<int:game_id>')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(UserGet, '/get_user')
api.add_resource(SelectPj, '/select')
api.add_resource(UserIdGet, '/get_id')
api.add_resource(Logout, '/logout')
