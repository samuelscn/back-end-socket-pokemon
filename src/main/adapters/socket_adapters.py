from src.main.factory.user.add_user_account_factory import AddUserAccountFactory
from src.main.factory.user.authenticate_user_factory import AuthenticateUserFactory

class SocketAdapters:
  def execute(self, socketRequest):
    if (socketRequest["route"] == 'user/create'):
      return AddUserAccountFactory.makeUserAccountFactory(socketRequest["body"])
    if (socketRequest["route"] == 'user/authenticate'):
      return AuthenticateUserFactory.makeAuthenticateUserFactory(socketRequest["body"])
