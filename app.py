from flask import Flask,render_template,url_for,request
import mongoengine
import pymongo

from mongoengine import *

# Config MongoDB
uri = "mongodb://admin:admin@ds119598.mlab.com:19598/cafeteria"
client = pymongo.MongoClient(uri)
db = client.get_default_database()

# Get MENU collection
menu_items = db["menu"].find()
menu_items_length = db["menu"].count()
print(menu_items[0])


class User(Document):
    name1 = StringField()
    desc1 = StringField()
    img1 = StringField()
    user1 = StringField()

app = Flask(__name__)

host ="ds133388.mlab.com"
port =33388
db_name="janeluong"
user_name="admin"
password="admin"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


@app.route('/')
def hello_world():
    return render_template("w3_About me.html")
@app.route('/zai')
def man():
    return render_template("w3_Manly Actors.html")

@app.route('/more',methods=["GET","POST"])
def more():
    if request.method == "GET":
        return(render_template("Addmore.html"))
    elif request.method=="POST":
        hname=request.form["name"]
        hdesc=request.form["desc"]
        himg=request.form["img"]
        contri=request.form["user"]

        user = User(name1=hname, desc1=hdesc,img1=himg,user1=contri)  # Constructor
        user.save()

        return render_template("thankyou.html")



if __name__ == '__main__':
    app.run()