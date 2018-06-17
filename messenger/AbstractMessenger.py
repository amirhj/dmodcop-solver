from abc import ABCMeta, abstractmethod

class AbstractMessenger(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.receiver = None

	@abstractmethod
	def send(self, agents, content):
		raise NotImplementedError()

	@abstractmethod
	def initReceiver(self):
		raise NotImplementedError()

	def setReceiver(self, receiver):
		self.receiver = receiver
		self.initReceiver()