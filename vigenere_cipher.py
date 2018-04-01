import math
from substitution_cipher import SubstitutionCipher

class VigenereCipher(SubstitutionCipher):

	def repeat_key(self, length):
		key_length = len(self.key)
		repeats = math.ceil(length/key_length)

		repeated_key = repeats * self.key
		repeated_key = repeated_key[:length]

		return repeated_key
