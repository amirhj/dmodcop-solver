from messenger import AbstractInitiator

class Initiator(AbstractInitiator):
	
	def __init__(self, agents, host, port, username, password):
		super().__init__(agents)
		self.host = host
		self.port = port
		self.username = username
		self.password = password