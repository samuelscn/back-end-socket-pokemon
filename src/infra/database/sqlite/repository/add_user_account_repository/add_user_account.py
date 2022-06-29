from src.infra.database.sqlite.views.user.user_view import *
from src.data.protocols.user.add_user_account_repository import AddUserAccountRepository as AddUserAccountRepositoryInterface

class AddUserAccountRepo(AddUserAccountRepositoryInterface):
  
  def add(self, accountUserData):
    insert(accountUserData)