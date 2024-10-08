import requests
import json
import datetime
from flask import Flask,jsonify, redirect, url_for, request,render_template
from dateutil.relativedelta import relativedelta

app = Flask(__name__)
port=5100

# line number 88 index.html

#high chastrts x axis and y axis


## transition in charts smooth -done
## input when backspaced and searched with new  - done
## make all calls when searched - done
## no makeupin json at backen - done

## css
# highchart labels, and all it's components.
# recommendations
## news info in the text part

# check when error condition occurs on news
# make default stock values as zero...

@app.route('/stocks_info')
def stocks_info():
   print(request,"S",request.args.get("name"));
   #print(requests.get("https://finnhub.io/api/v1/stock/profile2?symbol=TSLA&token=cms9s29r01qlk9b15gk0cms9s29r01qlk9b15gkg").content)
   url="https://finnhub.io/api/v1/stock/profile2?symbol="+request.args.get("name")+"&token=cms9s29r01qlk9b15gk0cms9s29r01qlk9b15gkg"
   return requests.get(url).content#jsonify(requests.get(url).content)  #"HI" #render_template("index.html")

@app.route('/sumamry_info')
def summary_info():
   url="https://finnhub.io/api/v1/quote?symbol="+request.args.get("name")+"&token=cms9s29r01qlk9b15gk0cms9s29r01qlk9b15gkg"
   return requests.get(url).content  #"HI" #render_template("index.html")

@app.route('/recmd_info')
def recmd_info():
   url="https://finnhub.io/api/v1/stock/recommendation?symbol="+request.args.get("name")+"&token=cms9s29r01qlk9b15gk0cms9s29r01qlk9b15gkg"
   return requests.get(url).content  #"HI" #render_template("index.html")




@app.route('/charts')
def charts():
   to= datetime.datetime.now().strftime('%Y-%m-%d')
   #from_d=(datetime.datetime.now() - datetime.timedelta(190) ).strftime('%Y-%m-%d')
   from_d=(datetime.datetime.now()+ relativedelta(months=-6)).strftime('%Y-%m-%d')
   url="https://api.polygon.io/v2/aggs/ticker/"+request.args.get("name").upper()+"/range/1/day/"+from_d+"/"+to+"?adjusted=true&sort=asc&apiKey=ctO8iVF_Gi19afBovU1ZSr6UIxqt8Fr3"
   print(url)
   data=requests.get(url).content 
   return data


@app.route('/news')
def news():
   to= datetime.datetime.now().strftime('%Y-%m-%d')
   from_d=(datetime.datetime.now() - datetime.timedelta(30) ).strftime('%Y-%m-%d')
   url="https://finnhub.io/api/v1/company-news?symbol="+request.args.get("name") + "&from="+from_d+"&to=" + to +"&token=cms9s29r01qlk9b15gk0cms9s29r01qlk9b15gkg"
   print(url)
   data=requests.get(url).content 
   return data

@app.route('/')
def homepage():
   print("DD")    
   return app.send_static_file("index.html");

if __name__ == '__main__':
	app.run()
