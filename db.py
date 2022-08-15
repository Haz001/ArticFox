import json
import soundex

class website:
	def __init__(self,id,name,domains,description):
		self.id = id
		self.name = name
		self.domains = domains
		self.description = description
	def __str__(self):
		msg = "ID:\t"+self.id+"\n"
		msg += "Name:\t"+self.name+"\n"
		msg += "Description:\n\t"+self.description+"\n"
		msg += "Domains:\n\t"+("\n\t").join(self.domains)
		return msg

def read_json(filename):
	file = open(filename)
	raw = file.read()
	file.close()
	json_data = json.loads(raw)
	return json_data

class db:
	websites = []
	
def setup(filename = "db.json"):
	obj = read_json(filename)
	websites_raw = (obj["website"])
	for wk,w in websites_raw.items():
		w_name = wk
		w_domains = [wk]
		w_description = "N/A"
		if("name" in w):
			w_name = w["name"]
		if("domains" in w):
			w_domains = w["domains"]
		if("description" in w):
			w_description = w["description"]
		w_t = website(wk,w_name,w_domains,w_description)
		db.websites.append(w_t)
