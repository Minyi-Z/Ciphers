from caesar_cipher import CaesarCipher
from substitution_cipher import SubstitutionCipher

cipher = SubstitutionCipher("b")
print(cipher.encipher("abc"))
print(cipher.decipher("bac"))