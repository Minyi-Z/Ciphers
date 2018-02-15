import pytest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from caesar_cipher import CaesarCipher

class TestCaesarCipher(object):
	@pytest.mark.parametrize("key", ["10", -1, 0, 26])
	def test_invalid_key(self, key):
		with pytest.raises(ValueError) as err_msg:
			CaesarCipher(key)
		assert str(err_msg.value) == "Key must be an integer between 1 and 25."

	def test_get_substitution_key(self):
		cipher = CaesarCipher(10)
		assert cipher.substitution == "klmnopqrstuvwxyzabcdefghij"

	def test_encipher(self):
		cipher = CaesarCipher(10)
		enciphered_msg = cipher.encipher("Abcd.efgHi#jklm noPQrstuv?Wxyz")
		assert enciphered_msg == "Klmn.opqRs#tuvw xyZAbcdef?Ghij"

	def test_decipher(self):
		cipher = CaesarCipher(10)
		deciphered_msg = cipher.decipher("Klmn.opqRs#tuvw xyZAbcdef?Ghij")
		assert deciphered_msg == "Abcd.efgHi#jklm noPQrstuv?Wxyz"