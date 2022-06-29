from src.presentation.errors.errors import Errors

class ListUserAccountController:
  def __init__ (self, listUserAccount):
    self.listUserAccount = listUserAccount

  def list (self, ):
    user_list = self.listUserAccount.get()
    return Errors.ok(user_list)