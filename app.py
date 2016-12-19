from flask import Flask,render_template,url_for,request
import mongoengine
import pymongo

from mongoengine import *

# Config MongoDB
#uri = "mongodb://admin:admin@ds133388.mlab.com:33388/janeluong"
#actor = pymongo.MongoClient(uri)
#db = actor.get_default_database()

class User(Document):
    name1 = StringField()
    desc1 = StringField()
    img1 = StringField()
    user1 = StringField()

app = Flask(__name__)

#data access:
#list: l[0]
#dictionary: d["name"]
#object: data + action

#OOP: Object Oriented Programming
class Ninja:
    def __init__(self,name,atk,def_,hp): #Constructor - xây dựng nên object
        self.name=name
        self.atk = atk
        self.def_ = def_
        self.hp = hp
    def print (self): #Context
        print("{0},{1},{2},{3}".format(self.name,self.atk,self.def_,self.hp))
    def attack (self,other):
        print("{0} is attacking {1}".format(self,other))
        if self.atk > other.def_:
            other.hp -= self.atk
        else:
            self.hp -= other.atk

#Init
ninja1 = Ninja("Naruto",10,9,8) #Ninja() -> __init__; ninja1 -> self
ninja2 = Ninja("Sasuke",9,6,7)
print(ninja1.atk)
print(ninja2.atk)

ninja1.atk = 10 # . -> of

print(ninja1.atk)
print(ninja2.atk)

ninja1.attack(ninja1)
ninja1.print()
ninja2.print()

host ="ds133388.mlab.com"
port =33388
db_name="janeluong"
user_name="admin"
password="admin"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

@app.route('/')
def hello_world():
    return render_template("w3_About me.html")


# Get USER collection
#user_more = db["user"].find()
#actor_list_length = db["user"].count()
#new_actors=user_more

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

@app.route('/zai')
def man():
    return render_template("w3_Manly Actors.html",new_actor = User.objects)

if __name__ == '__main__':
    app.run()