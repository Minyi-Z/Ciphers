from substitution_cipher import SubstitutionCipher

class PlayfairCipher(SubstitutionCipher):
	alphabet = "abcdefghiklmnopqrstuvwxyz"

	def __init__(self, key):
		super().__init__(key)
		self.substitution_table = self.get_substitution_table()

	def encipher(self, msg):
		enciphered_msg = []
		digraphs = self.form_digraphs(msg)

		for digraph in digraphs:
			enciphered_msg.append(self.substitute(digraph))

		return "".join(enciphered_msg)

	def decipher(self, msg):
		deciphered_msg = []
		digraphs = self.form_digraphs(msg)

		for digraph in digraphs:
			deciphered_msg.append(self.substitute(digraph, -1))

		deciphered_msg = list("".join(deciphered_msg))

		last_char = deciphered_msg[len(deciphered_msg) - 1] if deciphered_msg and not deciphered_msg[len(deciphered_msg) - 1] == 'x' else ""
			
		deciphered_msg = [deciphered_msg[i] for i in range(len(deciphered_msg) - 1) \
							if deciphered_msg[i] != "x" or deciphered_msg[i-1].lower() != deciphered_msg[i+1].lower()]

		deciphered_msg.append(last_char)

		return "".join(deciphered_msg)

	def form_digraphs(self, msg):
		digraphs = []
		msg = ''.join(msg.split())
		stripped_msg = ""

		for char in msg:
			if char == "j":
				stripped_msg += "i"
			elif char.isalpha():
				stripped_msg += char

		i = 0
		while i < len(stripped_msg):
			digraph = stripped_msg[i]
			if i == len(stripped_msg) - 1 or stripped_msg[i+1].lower() == stripped_msg[i].lower():
				digraph += "x"
				i+=1
			else:
				digraph += stripped_msg[i+1]
				i+=2
			digraphs.append(digraph)

		return digraphs

	def get_substitution_table(self):
		substitution = self.get_substitution()		
		return [[substitution[5*i+j] for j in range(5)] for i in range(5)]

	def substitute(self, digraph, shift = 1):
		enciphered_digraph = []
		letter1_coord = {}
		letter2_coord = {}

		for i, row in enumerate(self.substitution_table):
			for j, item in enumerate(row):
				if item == digraph[0].lower():
					letter1_coord = (i, j)
				if item == digraph[1].lower():
					letter2_coord = (i, j)

		if letter1_coord[0] == letter2_coord[0]:
			enciphered_digraph.append(self.substitution_table[letter1_coord[0]][(letter1_coord[1]+shift)%5])
			enciphered_digraph.append(self.substitution_table[letter2_coord[0]][(letter2_coord[1]+shift)%5])
		elif letter1_coord[1] == letter2_coord[1]:
			enciphered_digraph.append(self.substitution_table[(letter1_coord[0]+shift)%5][letter1_coord[1]])
			enciphered_digraph.append(self.substitution_table[(letter2_coord[0]+shift)%5][letter2_coord[1]])
		else:
			enciphered_digraph.append(self.substitution_table[letter1_coord[0]][letter2_coord[1]])
			enciphered_digraph.append(self.substitution_table[letter2_coord[0]][letter1_coord[1]])

		if digraph[0].isupper():
			enciphered_digraph[0] = enciphered_digraph[0].upper()
		if digraph[1].isupper():
			enciphered_digraph[1] = enciphered_digraph[1].upper()

		return "".join(enciphered_digraph)