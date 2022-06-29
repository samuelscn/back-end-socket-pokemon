from src.presentation.errors.errors import Errors

class ListTradeSolicitationsController:
  def __init__ (self, listTradeSolicitations):
    self.listTradeSolicitations = listTradeSolicitations

  def list (self, ):
    trade_list = self.listTradeSolicitations.get()
    return Errors.ok(trade_list)