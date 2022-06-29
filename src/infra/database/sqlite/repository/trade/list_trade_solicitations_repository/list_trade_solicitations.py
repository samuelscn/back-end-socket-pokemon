from src.data.protocols.trade.list_trade_solicitations_repository import ListTradeSolicitationsRepository as ListTradeSolicitationsRepositoryInterface
from src.infra.database.sqlite.views.trade.trade_view import *

class ListTradeSolicitationsRepo(ListTradeSolicitationsRepositoryInterface):
  
  def get (self, ):
    trade_solicitation_result = listTradeWithoutStatusFinished()
    print('trade_solicitation_result', trade_solicitation_result)
    if (trade_solicitation_result == None):
      return None
    return trade_solicitation_result