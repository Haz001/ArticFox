def replaceWithArray(needles, replacement, haystack):
	for needle in needles:
		haystack = haystack.replace(needle,replacement)
	return haystack
def sql_like_soundex(word):
	word = (word).lower()
	soundex = replaceWithArray(['a','e','i','o','u','y','h','w'],"0",word)
	soundex = replaceWithArray(['b','f','p','v'],"1",soundex)
	soundex = replaceWithArray(['c','g','j','k','q','s','x','z'],"2",soundex)
	soundex = replaceWithArray(['d','t'],"3",soundex)
	soundex = replaceWithArray(['l'],"4",soundex)
	soundex = replaceWithArray(['m','n'],"5",soundex)
	soundex = replaceWithArray(['r'],"6",soundex)
	last_letter = ''
	new_soundex = ''
	for s in soundex:
		if not(s == last_letter) or last_letter == '':
			new_soundex+=s
			last_letter = s
	soundex = new_soundex.replace("0","")
	while (len(soundex) < 4):
		soundex+='0'
	return word[0] + soundex[1:]
def normal_soundex(word):
	word = (word).lower()
	soundex = replaceWithArray(['a','e','i','o','u'],"0",word)
	soundex = replaceWithArray(['y','h','w'],"",soundex)
	soundex = replaceWithArray(['b','f','p','v'],"1",soundex)
	soundex = replaceWithArray(['c','g','j','k','q','s','x','z'],"2",soundex)
	soundex = replaceWithArray(['d','t'],"3",soundex)
	soundex = replaceWithArray(['l'],"4",soundex)
	soundex = replaceWithArray(['m','n'],"5",soundex)
	soundex = replaceWithArray(['r'],"6",soundex)
	last_letter = ''
	new_soundex = ''
	for s in soundex:
		if not(s == last_letter) and not(s == '0') or last_letter == '':
			new_soundex+=s
		last_letter = s
	soundex = new_soundex[:4]
	while (len(soundex) < 4):
		soundex+='0'
	return word[0] + soundex[1:]
soundex = normal_soundex
if __name__ == '__main__':
	print(soundex)
	while True:
		print(soundex(input("Soundexify:\n> _____\b\b\b\b\b")))

