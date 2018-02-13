from base_cipher import Cipher

class CaesarCipher(Cipher):
	def check_key(self):
		if not isinstance(self.key, int) or self.key not in range(1, 26):
			raise TypeError("Key must be an integer between 1 and 25.")
	
	def encipher(self, msg):
		enciphered_msg = ""

		for char in msg:
			if char.isalpha():
				enciphered_msg += chr(ord(char)+self.key)
			else:
				enciphered_msg += char

		return enciphered_msg

	def decipher(self, msg):
		return self.encipher(-self.key, msg)