def break_words(setence):
	"""This function wll break up words for us."""
	words = setence.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first words after popping if off."""
	word = words.pop(0)
	return word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	return words.pop(-1)

def sorted_setence(setence):
	"""Takes in a full sentence and returns sorted words."""
	words = break_words(setence)
	return sort_words(words)

def print_first_and_last(setence):
	"""Prints the first and last words of the sentence."""
	words = break_words(setence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(setence):
	"""Sorted the words then prints the first and last one."""
	words = sorted_setence(setence)
	print_first_word(words)
	print_last_word(words)