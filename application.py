from flask import Flask, render_template
import requests
from pyfiglet import Figlet
from termcolor import colored

app = Flask(__name__)

@app.route("/")
def index():
	response2 = requests.get("http://api.open-notify.org/astros.json")
	iss_now_res = requests.get("http://api.open-notify.org/iss-now.json") 
	iss_pass_res = requests.get("http://api.open-notify.org/iss-pass.json") 
	data2 = response2.json()
	f = Figlet(font='slant')
	human_in_space = "There is {} Astros in The Space".format(data2["number"])
	text = f.renderText(human_in_space)
	astros_in_space=[]
	for astros in data2["people"]:
		astros_in_space.append(astros["name"])
	iss_position = iss_now_res.json()
	longitude = iss_position["iss_position"]["longitude"]
	latitude = iss_position["iss_position"]["latitude"]

	return render_template("index.html",longitude=longitude,latitude=latitude, human_in_space=human_in_space, astros_in_space=astros_in_space )