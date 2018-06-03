from abc import ABCMeta, abstractmethod

class AbstractMessenger:
	__metaclass__ = ABCMeta

	def __init__(self):
		self.receiver = None
		super().__init__()

	@abstractmethod
	def send(self, agents, command):
		pass

	@abstractmethod
	def initReceiver(self):
		pass

	def setReceiver(self, receiver):
		self.receiver = receiver
		self.initReceiver()