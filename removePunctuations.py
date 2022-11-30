def removePunctuations(text) :
	punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
	
	for character in punctuation:
		text = text.replace(character, '')

	return text