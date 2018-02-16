import pytest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from playfair_cipher import PlayfairCipher

class TestPlayfairCipher(object):
	def test_form_digraphs(self):
		cipher = PlayfairCipher("A")
		assert cipher.form_digraphs("sHoOting stAr!!") == ["sH", "ox", "Ot", "in", "gs", "tA", "rx"]

	@pytest.mark.parametrize("digraph, expected_enciphered_digraph",[
							("bE", "cA"),
							("HX", "NC"),
							("gz", "kw")])
	def test_substitute(self, digraph, expected_enciphered_digraph):
		cipher = PlayfairCipher("A")
		assert cipher.substitute(digraph) == expected_enciphered_digraph

	def test_encipher(self):
		cipher = PlayfairCipher("IntErstellAr")
		assert cipher.encipher("Rage rage aGainSt the dYinG of tHe lIght.!?#@()") == "TchttchtgPstiLategihVetFwoeGnbTdge"

	def test_decipher(self):
		cipher = PlayfairCipher("IntErstellAr")
		assert cipher.decipher("TchttchtgPstiLategihVetFwoeGnbTdge") == "RagerageaGainStthedYinGoftHelIght"