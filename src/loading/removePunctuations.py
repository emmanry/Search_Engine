def removePunctuations(text) :
	'''
	Décompose le string en reçu en liste de mots, en retirant la ponctuation et les majuscules
	
	@inputs
		- text : mot ou groupe de mots.
	
	@output
		- liste de mots sans ponctuation ni majuscule.
	'''
	punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
	
	for character in punctuation:
		text = text.replace(character, ' ')

	return text.lower().strip().split()
