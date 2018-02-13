from base_cipher import Cipher

class CaesarCipher(Cipher):
	def check_key(self):
		if not isinstance(self.key, int):
			raise TypeError("key must be an integer")
	
	def encipher(self, msg):
		enciphered_msg = ""

		for letter in msg:
			enciphered_msg += chr(ord(letter)+self.key)

		return enciphered_msg

	def decipher(self, msg):
		return self.encipher(-self.key, msg)