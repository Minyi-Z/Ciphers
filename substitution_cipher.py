# each letter is replaced by another
# ciphertext alphabet defined by key
# duplicate letters removed from the key
# then if it is less than 26 letters, remaining letters are added on
# eg. key="interstellar", ciphertext_alphabet="interslabcdfghjkmopquvwxyz"

from base_cipher import Cipher

class SubstitutionCipher(Cipher):
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	def __init__(self, key):
		super().__init__(key)
		self.substitution = self.get_substitution()

	def check_key(self):
		if not isinstance(self.key, str) or not self.key.isalpha() or len(self.key) > 26:
			raise ValueError("Key must be a string consisting of between 1 and 26 letters")

	def encipher(self, msg):
		enciphered_msg = ""

		for char in msg:
			enciphered_msg += self.substitute(char, self.alphabet, self.substitution)

		return enciphered_msg

	def decipher(self, msg):
		deciphered_msg = ""

		for char in msg:
			deciphered_msg += self.substitute(char, self.substitution, self.alphabet)

		return deciphered_msg

	def get_substitution(self):
		lowercase_key = self.key.lower()
		substitution = ''.join(sorted(set(lowercase_key), key=lowercase_key.index))

		if len(substitution) < 26:
			for letter in self.alphabet:
				if letter not in substitution:
					substitution += letter
		
		return substitution

	def substitute(self, char, from_alphabet, to_alphabet):
		if char.isalpha():
			index = from_alphabet.index(char.lower())
			if char.isupper():
				return to_alphabet[index].upper()
			else:
				return to_alphabet[index]
		else:
			return char
