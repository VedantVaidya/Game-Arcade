import pymysql as p

def getconnection():
    return p.connect(host="localhost",user="root",password="",port=3306,database="gamearcade")


def adddata(t):
    c=getconnection()
    cur=c.cursor()
    sql="insert into info values(%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,t)
    c.commit()
    c.close()

def loginatt(id):
    c=getconnection()
    cur=c.cursor()
    qur="select password from info where id=%s"
    cur.execute(qur,id)
    a=cur.fetchall()
    c.commit()
    c.close()
    return(a)

def details(id):
    c=getconnection()
    cur=c.cursor()
    qur="select id,name,email,gender,highscore from info where id=%s"
    cur.execute(qur,id)
    a=cur.fetchall()
    c.commit()
    c.close()
    return(a[0])


def newhighscore(id,score):
    c=getconnection()
    cur=c.cursor()
    t=(score,id)
    qur="update info set highscore=%s where id=%s"
    cur.execute(qur,t)
    c.commit()
    c.close()

def detailsforadmin():
    c=getconnection()
    cur=c.cursor()
    qur="select * from info"
    cur.execute(qur)
    a=cur.fetchall()
    c.commit()
    c.close()
    return(a)

def toedit(id):
    c=getconnection()
    cur=c.cursor()
    qur="select * from info where id=%s"
    cur.execute(qur,id)
    a=cur.fetchall()
    c.commit()
    c.close()
    return(a[0])

def upd(t):
    c=getconnection()
    cur=c.cursor()
    qur="update info set id=%s,name=%s,email=%s,password=%s,gender=%s,highscore=%s where id=%s"
    cur.execute(qur,t)
    c.commit()
    c.close()

def deluser(id):
    c=getconnection()
    cur=c.cursor()
    qur="delete from info where id=%s"
    cur.execute(qur,id)
    c.commit()
    c.close()