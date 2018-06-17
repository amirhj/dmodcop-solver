from messenger import AbstractInitiator
from messenger.rabbitmq.Messenger import Messenger
import pika

class Initiator(AbstractInitiator):
	
	def __init__(self, agents, host, port, username, password):
		super().__init__(agents)
		self.host = host
		self.port = port
		self.username = username
		self.password = password
		self.init()
	
	def init(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
		self.channel = self.connection.channel()

		self.channel.exchange_declare(exchange='agent', exchange_type='topic')
		self.channel.exchange_declare(exchange='log', exchange_type='topic')
		self.channel.exchange_declare(exchange='command', exchange_type='topic')

		self.messengers = {}
		for a in self.agents:
			self.messengers[a] = Messenger(self.agents[a].neighbours, self.host, self.port, self.username, self.password)

