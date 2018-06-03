from abc import ABCMeta, abstractmethod

class AbstractLogger:
	__metaclass__ = ABCMeta

	def __init__(self):
		self.receiver = None
		super().__init__()

	@abstractmethod
	def write(self, agents, command):
		pass

	@abstractmethod
	def log(self):
		pass

	@abstractmethod
	def printLog(self, receiver):
		pass