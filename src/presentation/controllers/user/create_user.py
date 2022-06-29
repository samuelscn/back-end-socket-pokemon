
from src.domain.usecases.user.add_user_account import AddUserAccount

class CreateUserController:
  def __init__ (self, addUserAccount):
    self.addUserAccount = addUserAccount

  def handle (self, socketRequest):
    requiredFields = ['email', 'password', 'name']
  
    for fields in requiredFields:
      if socketRequest[fields] == None:
        return None
    self.addUserAccount.add(socketRequest)
    return 200