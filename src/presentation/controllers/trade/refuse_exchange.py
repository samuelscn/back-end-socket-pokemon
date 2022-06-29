from src.presentation.errors.errors import Errors

class RefuseExchangeController:
  def __init__ (self, refuseExchange):
    self.refuseExchange = refuseExchange

  def handle (self, socketRequest):
    self.refuseExchange.update(socketRequest["id"])
    return Errors.ok({})