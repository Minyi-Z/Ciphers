from substitution_cipher import SubstitutionCipher

class CaesarCipher(SubstitutionCipher):
	def check_key(self):
		if not isinstance(self.key, int) or self.key not in range(1, 26):
			raise ValueError("Key must be an integer between 1 and 25.")
	
	def get_substitution(self):
		substitution = ""

		for char in self.alphabet:
			char_sub_ascii = ord(char)+self.key
			if char_sub_ascii > ord('z'):
				char_sub_ascii -= 26
			substitution += chr(char_sub_ascii)

		return substitution
