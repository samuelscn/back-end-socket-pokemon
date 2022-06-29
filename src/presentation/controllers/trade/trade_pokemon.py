from src.presentation.errors.errors import Errors

class TradePokemonController:
  def __init__ (self, tradePokemon):
    self.tradePokemon = tradePokemon

  def handle (self, socketRequest):
    requiredFields = ['id','inventory_id', 'want_pokemon_id', 'give_pokemon_id']
  
    for fields in requiredFields:
      if socketRequest[fields] == None:
        return Errors.badRequest(f"Missing {fields} Field")
    self.tradePokemon.update(socketRequest)
    return Errors.ok({})