from abc import ABCMeta, abstractmethod

class AbstractMessageLogger:
	__metaclass__ = ABCMeta

	def __init__(self):
		super().__init__()

	@abstractmethod
	def initReceiver(self):
		pass