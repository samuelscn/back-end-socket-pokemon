from abc import ABC, abstractclassmethod

class ListTradeSolicitations(ABC):
	@abstractclassmethod
	def get (self, ):
		raise Exception("Should implement method")