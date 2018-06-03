from abc import ABCMeta, abstractmethod

class AbstractCommander:
	__metaclass__ = ABCMeta

	@abstractmethod
	def send(self, agents, command):
		pass

	@abstractmethod
	def initExecuter(self):
		pass

	def setExecuter(self, executer):
		self.executer = executer
		self.initExecuter()