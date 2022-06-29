from abc import ABC, abstractclassmethod

class ListUserAccountRepository(ABC):
  @abstractclassmethod
  def get (self, ):
    raise Exception("Should implement method")