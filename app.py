from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape2
import os




app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():

      mars_info = mongo.db.mars_info.find_one()
    
      return render_template("index1.html",mars_info = mars_info)

@app.route("/scrape")
def scrape():

      mars_info = mongo.db.mars_info
      mars_data = mars_scrape2.scrape_all()
      mars_info.replace_one({}, mars_data, upsert=True)
      
      return redirect("/", code=302)

if __name__== "__main__":
    app.run(debug=True)    
