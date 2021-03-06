from flask import Flask, render_template
from datetime import *
from pytz import timezone
import hashlib

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html', color=get_color())

def get_color():
	hashy = hashlib.sha1()
	hashy.update(datetime.today().replace(tzinfo=timezone('EST')).strftime("%D"))
	return hashy.hexdigest()[-6:]

if __name__ == "__main__":
	app.run()

