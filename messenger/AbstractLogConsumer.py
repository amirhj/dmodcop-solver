from abc import ABCMeta, abstractmethod

class AbstractLogConsumer:
	__metaclass__ = ABCMeta

	def __init__(self):
		super().__init__()

	@abstractmethod
	def initConsumer(self):
		pass