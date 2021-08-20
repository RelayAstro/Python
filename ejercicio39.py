#The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?
def highlight_word(sentence, word):
	ind = sentence.index(word)
	tamaño = len(word)
	arreglado = sentence[:ind] + word.upper() + sentence[ind + tamaño:]
	return(arreglado)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))