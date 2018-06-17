from messenger import AbstractMessenger
import pika

class Messenger(AbstractMessenger):

	def __init__(self, connectedAgents, host, port, username, password):
		super().__init__()

		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
		self.channel = self.connection.channel()
		self.connectedAgents = connectedAgents
	
	def send(self, agents, content):
		for a in agents:
			self.channel.basic_publish(exchange='agents', routing_key=a, body=content)
	
	def initReceiver(self):
		result = self.channel.queue_declare(exclusive=True)
		self.queueName = result.method.queue

		for bindingKey in self.connectedAgents:
			self.channel.queue_bind(exchange='agents', queue=self.queueName, routing_key=bindingKey)
		
		self.channel.queue_bind(exchange='commands', queue=self.queueName, routing_key=bindingKey)

		callbackHandler = self.mailboxHandler
		self.channel.basic_consume(callbackHandler, queue=self.queueName, no_ack=True)
	
	def mailboxHandler(self, channel, method, properties, body):
		messageType = method.exchange[:-1]
		source = method.routing_key
		self.receiver(messageType, source, body)
