from abc import ABCMeta, abstractmethod

class AbstractExecuter:
	__metaclass__ = ABCMeta

	def __init__(self):
		self.executer = None
		super().__init__()

	@abstractmethod
	def initExecuter(self):
		pass

	def setExecuter(self, executer):
		self.executer = executer