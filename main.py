from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')


@app.route('/s/',methods=['get'])
def search():
	message = ""
	search = str(request.args.get('q', ''))
	return message, 201

