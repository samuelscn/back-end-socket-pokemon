from src.infra.database.sqlite.views.user.user_view import *
from src.data.protocols.user.authenticate_user_repository import AuthenticateUserRepository as AuthenticateUserRepositoryInterface
from src.data.protocols.user.list_user_account_repository import ListUserAccountRepository as ListUserAccountRepositoryInterface

class ListUserAccountRepo(ListUserAccountRepositoryInterface):
  
  def get (self, ):
    user_result = list()
    print('user_result', user_result)
    if (user_result == None):
      return None
    user_dict = []
    for user in user_result:
      user_dict.append(
        { 
          "id": user[0],
          "username": user[1],
          "name": user[3]
        }
      )
    return user_dict