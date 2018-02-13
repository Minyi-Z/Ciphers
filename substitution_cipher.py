from base_cipher import Cipher

class SubstitutionCipher(Cipher):
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	def __init__(self, key):
		super().__init__(key)
		self.substitution = self.get_substitution()

	def check_key(self):
		if not isinstance(self.key, str) or not self.key.isalpha() or len(self.key) > 26:
			raise TypeError("Key must consist of letters and be less than or equal to 26 characters.")

	def encipher(self, msg):
		enciphered_msg = ""

		for char in msg:
			if char.isalpha():
				index = self.alphabet.index(char)
				enciphered_msg += self.substitution[index]
			else:
				enciphered_msg += char

		return enciphered_msg

	def decipher(self, msg):
		deciphered_msg = ""

		for char in msg:
			if char.isalpha():
				index = self.substitution.index(char)
				deciphered_msg += self.alphabet[index]
			else:
				deciphered_msg += char

		return deciphered_msg

	def get_substitution(self):
		substitution = self.key

		for letter in self.alphabet:
			if letter not in substitution:
				substitution += letter
		
		return substitution