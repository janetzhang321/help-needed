import plotly.plotly as py
import plotly.tools as tls
from urllib2 import urlopen
import os
tls.set_credentials_file(username='farhan3231', api_key=open(os.getcwd() + '/apiKey.txt').read().split("\n")[1])
from apiManager import censusAPIManager

url="http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:*&LAN=625"

#takes in url, gets you the data
def urlparser(url):
    x = url.split("/")
    return censusAPIManager('https://api.census.gov/data/').getAPIData(x[4],x[5]+'/'+x[6])

#makes map colorful
scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
       [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

#converts census sublists into single data array
def dataToList(result):
    result = sorted(result)
    x = []
    for d in result:
        if d[0] == "NAME" or d[0] == "District of Columbia" or d[0] == "Puerto Rico" or d[0] =="STABREV" or d[0] =="DC" or d[0] =="PR":
            continue
        x.append(d[1])
    return x

#turns every element in a list to '0'
def blanker(x):
    n=len(x)-1
    while n > -1:
        x[n] = '0'
        n -= 1

def mapMaker(url,fname):
	states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
		  
	data = [ dict(
		type='choropleth',
		colorscale = scl,
		autocolorscale = False,
		locations = states,
		z = dataToList(urlparser(url)),
		locationmode = 'USA-states',
		text = "random",
		marker = dict(
			line = dict (
				color = 'rgb(255,255,255)',
				width = 2
			) ),
		colorbar = dict(
			title = fname)
	) ]

	layout = dict(
		title = fname,
		geo = dict(
			scope='usa',
			projection=dict( type='albers usa' ),
			showlakes = True,
			lakecolor = 'rgb(255, 255, 255)'),
	)

	fig = dict( data=data, layout=layout )
	py.plot(fig, filename=fname)
