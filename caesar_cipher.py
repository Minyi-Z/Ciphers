from base_cipher import Cipher

class CaesarCipher(Cipher):
	def check_key(self):
		if not isinstance(self.key, int) or self.key not in range(1, 26):
			raise ValueError("Key must be an integer between 1 and 25.")
	
	def encipher(self, msg):
		enciphered_msg = ""

		for char in msg:
			if char.isalpha():
				new_char_ascii = ord(char)+self.key
				if new_char_ascii > ord('z'):
					new_char_ascii -= 26
				enciphered_msg += chr(new_char_ascii)
			else:
				enciphered_msg += char

		return enciphered_msg

	def decipher(self, msg):
		deciphered_msg = ""

		for char in msg:
			if char.isalpha():
				new_char_ascii = ord(char)-self.key
				if new_char_ascii < ord('a'):
					new_char_ascii += 26
				deciphered_msg += chr(new_char_ascii)
			else:
				deciphered_msg += char

		return deciphered_msg