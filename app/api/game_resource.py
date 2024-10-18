from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from game.controllers.district_controller import DistrictController
from game.controllers.game_controller import GameController
from game.logic.game_logic import GameLogicSchema

games = {}

class ConfigDistrict(Resource):    
    def get(self):
        controller = DistrictController()
        default_district = controller.get_new_district()
        return default_district

    @jwt_required()
    def post(self):
        data = request.get_json()
        controller = GameController()
        new_game = controller.get_game(data)        
        if isinstance(new_game, str):
            return { 'error': new_game }, 400
        game_id = get_jwt_identity()
        games[game_id] = new_game
        return { 'game_id': game_id }

class Game(Resource):
    def put(self, game_id):
        game_id = int(game_id)
        if game_id > 0:
            curr_game = games[game_id]
            schema = GameLogicSchema()
            controller = GameController()
            health_district = controller.life_of_each_district(curr_game)
            #lifes_tributes = controller.life_of_each_tribute(current_game)
            return { game_id: schema.dump(curr_game),
                    'health': health_district }
        return { 'error': 'Game not found' }, 404
          
    def get(self, game_id):
        game_id = int(game_id)
        if game_id > 0:
            curr_game = games[game_id]
            controller = GameController() 
            next_iteration = controller.get_one_iteration(curr_game)
            live_district = controller.pause_game(curr_game)
            health_district = controller.life_of_each_district(curr_game)
            #lifes_tributes = controller.life_of_each_tribute(current_game)
            return { game_id: next_iteration,
                    'pause': live_district,
                    'health': health_district }
        return { 'error': 'Game not found' }, 404