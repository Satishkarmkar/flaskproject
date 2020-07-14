from flask import Flask
from flask import render_template
from flask import request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/admin')
def admin_login_page():
    return render_template('admin_login.html')

@app.route('/validate_admin',methods=['POST'])
def validateAdmin():
   uname = request.form.get("t1")
   upass = request.form.get("t2")

   if uname =="satish" and upass == "Satish@3118":
       return render_template('admin_welcome.html')

   else:
       mess = {"error": "Invalid User"}
       return render_template("admin_login.html", message=mess)

@app.route('/admin_home')
def adminHome():
    return render_template('admin_welcome.html')

@app.route('/schedule_new_class')
def scheduleNewClass():
    return render_template('schedule_new_class.html')

@app.route('/save_course',methods = ['POST'])
def save_course():
    cno = request.form.get("c0")
    cname = request.form.get("c1")
    fname = request.form.get("c2")
    date = request.form.get("c3")
    time = request.form.get("c4")
    fee = request.form.get("c5")
    dur = request.form.get("c6")

    conn = sql.connect("onlineclasses.sqlite2")
    curs = conn.cursor()
    curs.execute("select max(cno) from course")
    res = curs.fetchone()

    if res[0]:
        cno = res[0]+1
    else:
        cno = 1001

    curs.execute("insert into course values (?,?,?,?,?,?,?)",(cno,cname,fname,date,time,fee,dur))
    conn.commit()
    conn.close()

    return render_template('schedule_new_class.html' ,message='New class saved')


@app.route('/show_all_schedule_class')
def showAllScheduleClass():
    return render_template('show_all_schedule_class.html')

if __name__ == '__main__':
    app.run(debug=True)
