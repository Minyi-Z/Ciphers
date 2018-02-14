import pytest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from caesar_cipher import CaesarCipher

class TestCaesarCipher(object):
	def test_no_key(self):
		with pytest.raises(TypeError):
			CaesarCipher()

	@pytest.mark.parametrize("key", ["10", -1, 0, 26])
	def test_invalid_key(self, key):
		with pytest.raises(ValueError) as err_msg:
			CaesarCipher(key)
		assert str(err_msg.value) == "Key must be an integer between 1 and 25."

	def test_encipher(self):
		cipher = CaesarCipher(10)
		enciphered_msg = cipher.encipher("abcdefghijklmnopqrstuvwxyz")
		assert enciphered_msg == "klmnopqrstuvwxyzabcdefghij"

	def test_decipher(self):
		cipher = CaesarCipher(10)
		deciphered_msg = cipher.decipher("klmnopqrstuvwxyzabcdefghij")
		assert deciphered_msg == "abcdefghijklmnopqrstuvwxyz"