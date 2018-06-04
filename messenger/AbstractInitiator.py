from abc import ABCMeta, abstractmethod

class AbstractInitiator:
	__metaclass__ = ABCMeta

	def __init__(self, agents):
		self.agents = agents
		super().__init__()

	@abstractmethod
	def getCommander(self):
		pass

	@abstractmethod
	def getExecuters(self):
		pass

	@abstractmethod
	def getLogger(self):
		pass

	@abstractmethod
	def getMessengers(self):
		pass

	@abstractmethod
	def getLogConsumer(self):
		pass

	@abstractmethod
	def getMessageLogger(self):
		pass