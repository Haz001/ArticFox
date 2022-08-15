from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello world"


@app.route('/s/',methods=['POST','get'])
def search():
	message = ""
	try:
		response = {}
		response["method"] = str(request.method)
		response["query"] = str(request.form['q'])
		message = "Message"+str(response)
	except Exception as e:
		message = str(e)
	return message, 201

