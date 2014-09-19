from flask import Flask
from datetime import date
import hashlib

app = Flask(__name__)

@app.route("/")
def hello():
	get_color()
	return "Hello World!"

def get_color():
	today = date.today()
	hashy = hashlib.sha1()
	hashy.update(today)
	print hashy 

if __name__ == "__main__":
	app.run()

