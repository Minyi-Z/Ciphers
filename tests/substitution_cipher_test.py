import pytest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from substitution_cipher import SubstitutionCipher

class TestSubstitutionCipher(object):
	def test_no_key(self):
		with pytest.raises(TypeError):
			SubstitutionCipher()

	@pytest.mark.parametrize("key", [-1, True, "", "bad key", "{9*ah$%" "alkshfakshdausdojshkjdosiehcoieroaiejf"])
	def test_invalid_key(self, key):
		with pytest.raises(ValueError) as err_msg:
			SubstitutionCipher(key)
		assert str(err_msg.value) == "Key must be a string consisting of between 1 and 26 letters"

	@pytest.mark.parametrize("key, expected_substitution", [
							("repeat", "repatbcdfghijklmnoqsuvwxyz"),
							("qweRtyuiopasdFghjKlzxcvBnm", "qwertyuiopasdfghjklzxcvbnm"),
							("qwErtY", "qwertyabcdfghijklmnopsuvxz")])
	def test_get_substitution_key(self, key, expected_substitution):
		cipher = SubstitutionCipher(key)
		assert cipher.substitution == expected_substitution
	
	def test_encipher(self):
		cipher = SubstitutionCipher("qwerty")
		enciphered_msg = cipher.encipher("Do not go gentle into that good night.!?#@()")
		assert enciphered_msg == "Rj ijo aj atiogt cioj obqo ajjr icabo.!?#@()"

	def test_decipher(self):
		cipher = SubstitutionCipher("qwerty")
		deciphered_msg = cipher.decipher("Rj ijo aj atiogt cioj obqo ajjr icabo.!?#@()")
		assert deciphered_msg == "Do not go gentle into that good night.!?#@()"