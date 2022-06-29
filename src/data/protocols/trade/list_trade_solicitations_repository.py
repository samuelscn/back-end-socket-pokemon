from abc import ABC, abstractclassmethod

class ListTradeSolicitationsRepository(ABC):
  @abstractclassmethod
  def get (self, ):
    raise Exception("Should implement method")