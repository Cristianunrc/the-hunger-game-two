from game.logic.game_logic import GameLogic, GameLogicSchema, GameMode

class GameController:
      # Set up a game.  
      def get_game(self, data):
        game = GameLogic()
        game.new_game(15, 15)
        try:
            game.set_parameters(data['life'], data['force'], data['alliance'], data['cant_tributes'], data['cowardice'])
        except ValueError as event:
            return str(event)
        game.configure_random_districts()
        game.distribute_district_tributes()
        game.distribute_neutral_tributes(10)
        game.distribute_items()
        game.mode = GameMode.SIMULATION
        return game

      # This method takes the current state of game, do an iteration, and
      # return the update state serialized in readable format. 
      def get_one_iteration(self, game: GameLogic):
        next_iteration = game.one_iteration_front()
        if next_iteration is None:
            return {"error": "No data for next iteration"}
        next_iteration.winner_district()
        schema = GameLogicSchema()
        
        result = schema.dump(next_iteration)
        
        return result
      
      # Return one list of number lives tributes for each district's 
      def pause_game(self, current_game):
          lives = current_game.tributes_lives()
          return lives
      
      # Return one list of health of each distric's 
      def life_of_each_district(self, current_game):
          district_life = current_game.district_lifes()
          return district_life
      
    #   def life_of_each_tribute(self, current_game):
    #       lifes = current_game.live_and_dead_tributes()
    #       return lifes
      