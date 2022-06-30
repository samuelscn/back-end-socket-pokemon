from src.data.protocols.trade.trade_pokemon_repository import TradePokemonRepository as TradePokemonRepositoryInterface
from src.infra.database.sqlite.views.trade.trade_view import *
from src.infra.database.sqlite.views.inventory.inventory_view import *

class TradePokemonRepo(TradePokemonRepositoryInterface):
  
  def update (self, tradeData):
    solicitation_result = getOneSolicitation(tradeData)
    solic_dict = {
      "want_pokemon_id": solicitation_result[3],
      "give_pokemon_id": solicitation_result[4]
    }
    inventory_sender_user_result = getInventoryAndUserData(solicitation_result[2])
    tradePokemon(solic_dict, inventory_sender_user_result[0])
    inventory_received_user_result = getInventoryAndUserData(solicitation_result[1])
    secondTradePokemon(solic_dict, inventory_received_user_result[0])
    updateTradeStatus(tradeData)