from src.data.protocols.trade.trade_pokemon_repository import TradePokemonRepository as TradePokemonRepositoryInterface
from src.infra.database.sqlite.views.trade.trade_view import *
from src.infra.database.sqlite.views.inventory.inventory_view import *

class TradePokemonRepo(TradePokemonRepositoryInterface):
  
  def update (self, tradeData):
    inventory_sender_user_result = getInventoryAndUserData(tradeData["sender_user_id"])
    tradePokemon(tradeData, inventory_sender_user_result[0])
    inventory_received_user_result = getInventoryAndUserData(tradeData["received_user_id"])
    secondTradePokemon(tradeData, inventory_received_user_result[0])
    updateTradeStatus(tradeData["id"])