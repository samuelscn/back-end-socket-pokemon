from abc import ABC, abstractclassmethod

class ListUserAccount(ABC):
	@abstractclassmethod
	def get (self, ):
		raise Exception("Should implement method")