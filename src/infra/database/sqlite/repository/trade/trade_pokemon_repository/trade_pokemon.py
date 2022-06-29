from src.data.protocols.trade.trade_pokemon_repository import TradePokemonRepository as TradePokemonRepositoryInterface
from src.infra.database.sqlite.views.trade.trade_view import *

class TradePokemonRepo(TradePokemonRepositoryInterface):
  
  def update (self, tradeData):
    tradePokemon(tradeData)
    updateTradeStatus(tradeData["id"])