from flask import Flask, render_template, request
from utils import map

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/10.embed?autosize=True&link=false&modebar=false")
	
@app.route("/spanish")
def spanish():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/0.embed?autosize=True&link=false&modebar=false")
	
@app.route("/french")
def french():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/2.embed?autosize=True&link=false&modebar=false")
	
@app.route("/portuguese")
def portuguese():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/6.embed?autosize=True&link=false&modebar=false")
	
@app.route("/german")
def german():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/4.embed?autosize=True&link=false&modebar=false")

@app.route("/state")
def state():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/8.embed?autosize=True&link=false&modebar=false")
	
@app.route("/insured")
def insured():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/14.embed?autosize=True&link=false&modebar=false")
	
@app.route("/uninsured")
def uninsured():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/16.embed?autosize=True&link=false&modebar=false")

@app.route("/poverty")
def poverty():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/18.embed?autosize=True&link=false&modebar=false")

@app.route("/poverty04")
def poverty04():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/20.embed?autosize=True&link=false&modebar=false")
	
@app.route("/poverty517")
def poverty517():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/22.embed?autosize=True&link=false&modebar=false")

@app.route("/povertyMOE")
def povertyMOE():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/28.embed?autosize=True&link=false&modebar=false")

@app.route("/poverty04MOE")
def poverty04MOE():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/30.embed?autosize=True&link=false&modebar=false")
	
@app.route("/poverty517MOE")
def poverty517MOE():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/32.embed?autosize=True&link=false&modebar=false")
	
	
@app.route("/householdincome")
def householdincome():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/24.embed?autosize=True&link=false&modebar=false")
	
@app.route("/householdincomeerror")
def householdincomeerror():
    return render_template("map.html", url = "https://plot.ly/~farhan3231/26.embed?autosize=True&link=false&modebar=false")
	
@app.route("/<path:censusURL>")
def renderFilteredData(censusURL):
	censusURL = censusURL.split('$')
	return render_template("map.html", url = map.mapMaker(censusURL[1],censusURL[0]))

if __name__ == '__main__':
    app.debug = True
    app.run()
