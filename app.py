from flask import *
import dbm
import datetime as d
app=Flask(__name__,static_folder='static')

class idgen:
    def idgenerator(a):
        alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        y=alpha.index((a[1]))
        b = d.datetime.now()
        c=str(b)
        id=c[11:13]+c[14:16]+str(y)
        return(id)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/registeratt",methods=["post"])
def registeratt():
    name=request.form["name"]
    id=idgen.idgenerator(name)
    email=request.form["email"]
    password=request.form["password"]
    gender=request.form["gender"]
    highscore=0
    t=(id,name,email,password,gender,highscore)
    dbm.adddata(t)
    print(name,email,password,gender,id)
    return render_template("regsuccess.html",id=id)


@app.route("/loginatt",methods=["post"])
def loginatt():
    id=request.form["userid"]
    password=request.form["password"]
    passcheck=dbm.loginatt(id)
    if len(passcheck) == 0:
        return redirect("/login")
    elif password in passcheck[0]: 
        return redirect(f"/home?id={id}")
    return redirect("/login")  

@app.route("/home")
def home():
    id=request.args.get("id")
    t=dbm.details(id) 
    return render_template("home.html",t=t)

@app.route("/choosecharacter")
def choosecharacter():
    id=request.args.get("id")
    t=dbm.details(id)
    return render_template("choosecharacter.html",t=t)

@app.route("/play")
def play():
    id=request.args.get("id")
    char=request.args.get("char")
    t=dbm.details(id) 
    return render_template("play.html",t=t,char=char)


@app.route("/scoresubmit")
def submitscore():
    id=request.args.get("id")
    score=int(request.args.get("score"))

    print(id,score)
    t=dbm.details(id) 
    if(score>t[4]):
        dbm.newhighscore(id,score)
    return redirect(f"/home?id={t[0]}") 


@app.route("/adminlogin")
def adminlogin():
    return render_template("adminlogin.html")

@app.route("/addlog",methods=["post"])
def addlog():
    adminkey=request.form["adminkey"]
    if adminkey=="vedantthegreatestvaidya":
        return redirect("/admin")
    else:
        return redirect("/adminlogin")

@app.route("/admin")
def admin():
    a=dbm.detailsforadmin()
    return render_template("admin.html",t=a)

@app.route("/edit")
def edit():
    id=request.args.get("id")
    a=dbm.toedit(id)
    return render_template("edit.html",i=a)

@app.route("/update", methods=["post"])
def update():
    id=request.form["id"]
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    highscore=request.form["highscore"]
    gender=request.form["gender"]
    t=(id,name,email,password,gender,highscore,id)
    dbm.upd(t)
    return redirect("/admin")

@app.route("/del")
def dele():
    id=request.args.get("id")
    dbm.deluser(id)
    return redirect("/admin")


if __name__=="__main__":
    app.run(debug=True)


#create database gamearcade;
#create table info(id int,name varchar(30),email varchar(30),password varchar(30),gender varchar(10),highscore int);
