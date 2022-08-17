import json
import soundex




class Keywords:
	def __init__(self, *other):
		self.keywords = []
		self.s_keywords = []
		for w in other:
			self.append(w)
	def __contains__(self, item):
		for k in self.keywords:
			if item in k:
				return True
		return False
	def similar_to(self,item):
		return (soundex.soundex(item) in self.s_keywords)

	def append(self, other):
		if(type(other) == str):
			for w in other.split(" "):
				self.keywords.append(w.lower())
				sx = soundex.soundex(w)
				if(sx != None):
					self.s_keywords.append(sx)
		elif(other == None):
			pass
		else:
			raise "Type Error"
	def join(self,other:list):
		for w in other:
			self.append(w)

	def __str__(self):
		return " ".join(self.keywords)

class WebSite:
	def __init__(self, id:str, name:str, domains:list, description:str):
		self.id = id
		self.name = name
		self.domains = domains
		self.description = description
		self.keywords = Keywords(id,name,description)
		self.keywords.join(domains)

	def __str__(self):
		msg = "ID:\t" + self.id + "\n"
		msg += "Name:\t" + self.name + "\n"
		msg += "Description:\n\t" + self.description + "\n"
		msg += "Domains:\n\t" + ("\n\t").join(self.domains)
		return msg

class WebPage:
	def __init__(self, website: WebSite, url: str, title: str, description: str, tags: list, h1: list):
		self.keywords = Keywords()
		self.website = website
		self.keywords.append(website)
		self.url = url
		self.keywords.append(url)
		self.title = title
		self.keywords.append(title)
		self.description = description
		self.keywords.append(description)
		self.tags = tags
		self.keywords.join(tags)
		self.h1 = h1
		self.keywords.join(h1)

	def __str__(self):
		msg = ""
		if(self.website != None):
			msg += "Website:\t" + self.website + "\n"
		else:
			msg+= "Website:\t Unknown\n"

		msg += "URL:\t" + self.url + "\n"
		msg += "Title:\t" + self.url + "\n"
		msg += "Description:\n\t" + self.description + "\n"
		msg += "Tags:\n\t" + ("\n\t").join(self.tags)+"\n"
		msg += "H1:\n\t" + ("\n\t").join(self.h1)
		return msg


class db:
	websites = []
	webpages = []


def read_json(filename):
	file = open(filename)
	raw = file.read()
	file.close()
	json_data = json.loads(raw)
	return json_data


def parse_websites(websites_raw :dict):
	w_array = []
	for wk, w in websites_raw.items():
		w_name = wk
		w_domains = [wk]
		w_description = "N/A"
		if ("name" in w):
			w_name = w["name"]
		if ("domains" in w):
			w_domains = w["domains"]
		if ("description" in w):
			w_description = w["description"]
		w_t = WebSite(wk, w_name, w_domains, w_description)
		w_array.append(w_t)
	return w_array


def parse_webpages(webpages_raw :list,websites_array:list):
	p_array = []
	for p in webpages_raw:
		p_site = None
		p_url = None
		p_title = None
		p_description = "N/A"
		p_tags = []
		p_h1 = []
		if ("website" in p):
			for w in websites_array:
				if(w.name == p["website"]):
					p_site = w
				else:
					p_site = None
		if ("url" in p):
			p_url = p["url"]
		if ("title" in p):
			p_title = p["title"]
		if ("description" in p):
			p_description = p["description"]
		if ("tags" in p):
			p_tags = p["tags"]
		if ("h1" in p):
			p_h1 = p["h1"]
		p_t = WebPage(p_site, p_url, p_title, p_description, p_tags, p_h1)
		p_array.append(p_t)
	return p_array


def setup(filename="db.json"):
	obj = read_json(filename)
	db.websites = parse_websites(obj["website"])
	db.webpages = parse_webpages(obj["webpage"], db.websites)
	# for w in db.websites:
	# 	print("-"*16)
	# 	print(w)
	# for p in db.webpages:
	# 	print("-"*16)
	# 	print(p)


def search(needle, haystack):
	results = []
	for n in needle.split(" "):
		if(len(n)> 0):
			for haybale in haystack:
				if(haybale not in results):
					if(n in haybale.keywords):
						results.append(haybale)
					elif(haybale.keywords.similar_to(n)):
						results.append(haybale)
	return results
if __name__ == "__main__":
	setup('db.json')
	q = input("Search:\n> ")
	print("Websites:")
	for w in (search(q,db.websites)):
		print("\t"+w.name+" - "+", ".join(w.domains)+"\n")
	print("Webpages:")
	for p in (search(q,db.webpages)):
		print("\t"+p.title+" - "+p.url+"\n")
	# search(input(),db.webpage)
	#print(type(db.websites[0]) == WebSite)
	kr = ""
	for w in db.websites:
		kr += str(w.keywords) + " "
	for p in db.webpages:
		kr += str(p.keywords) + " "
	t_kw = kr.split(" ")
	del kr
	kw = []
	for k in t_kw:
		if(k not in kw) or (k == ""):
			kw.append(k)
	print("; ".join(kw))