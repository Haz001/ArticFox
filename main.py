from flask import Flask
from flask import request
from flask import render_template

import db

db.setup("db.json")

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')


@app.route('/s/',methods=['get'])
def search():
	message = ""
	search = str(request.args.get('q', ''))
	message+=("Websites:<br/>")
	for w in (db.search(search,db.db.websites)):
		message+=("\t"+w.name+" - "+", ".join(w.domains)+"<br/>")
	message+=("Webpages:<br/>")
	for p in (db.search(search,db.db.webpages)):
		message+=("\t"+p.title+" - "+p.url+"<br/>")
	return message, 201

