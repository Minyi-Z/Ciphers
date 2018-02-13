from abc import ABC, abstractmethod

class Cipher(ABC):
	def __init__(self, key):
		self.key = key
		self.check_key()

	@abstractmethod
	def check_key(self):
		pass
	
	@abstractmethod
	def encipher(self, msg):
		pass

	@abstractmethod
	def decipher(self, msg):
		pass
	