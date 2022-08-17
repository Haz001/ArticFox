normal_0 = ['a','e','i','o','u']
sql_0 = [*normal_0,'y','h','w']
normal_1 = ['y','h','w']
letters1 = ['b','f','p','v']
letters2 = ['c','g','j','k','q','s','x','z']
letters3 = ['d','t']
letters4 = ['l']
letters5 = ['m','n']
letters6 = ['r']
def replaceWithArray(needles, replacement, haystack):
	for needle in needles:
		haystack = haystack.replace(needle,replacement)
	return haystack
def sql_like_soundex(word):
	word = (word).lower()
	soundex = replaceWithArray(sql_0,"0",word)
	soundex = replaceWithArray(letters1,"1",soundex)
	soundex = replaceWithArray(letters2,"2",soundex)
	soundex = replaceWithArray(letters3,"3",soundex)
	soundex = replaceWithArray(letters4,"4",soundex)
	soundex = replaceWithArray(letters5,"5",soundex)
	soundex = replaceWithArray(letters6,"6",soundex)
	last_letter = ''
	new_soundex = ''
	for s in soundex:
		if not(s == last_letter) or last_letter == '':
			new_soundex+=s
			last_letter = s
	soundex = new_soundex.replace("0","")
	while (len(soundex) < 4):
		soundex+='0'
	if(len(soundex) > 2):
		return word[0] + soundex[1:]
	else:
		return word[0]


def normal_soundex(word):
	word = (word).lower()
	soundex = replaceWithArray(normal_0,"0",word)
	soundex = replaceWithArray(normal_1,"",soundex)
	soundex = replaceWithArray(letters1,"1",soundex)
	soundex = replaceWithArray(letters2,"2",soundex)
	soundex = replaceWithArray(letters3,"3",soundex)
	soundex = replaceWithArray(letters4,"4",soundex)
	soundex = replaceWithArray(letters5,"5",soundex)
	soundex = replaceWithArray(letters6,"6",soundex)
	last_letter = ''
	new_soundex = ''
	for s in soundex:
		if not(s == last_letter) and not(s == '0') or last_letter == '':
			new_soundex+=s
		last_letter = s
	soundex = new_soundex[:4]
	while (len(soundex) < 4):
		soundex+='0'
	if(len(word) == 0):
		return ""
	if(len(soundex) > 2):
		return word[0] + soundex[1:]
	else:
		return word[0]

def parse(word):
	parsed = ""
	for l in word.lower():
		if(ord(l) in range(97,123)):
			parsed+=l
	if not (parsed == None):
		return parsed
	else:
		return None

def soundex(word):
	parsed = parse(word)
	if(parsed != None):
		return normal_soundex(parsed)
	else:
		return None

if __name__ == '__main__':
	print(soundex)
	while True:
		print(soundex(input("Soundexify:\n> _____\b\b\b\b\b")))

