from flask import Flask,render_template,redirect,request,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'monitoring_database'

mysql = MySQL(app)

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/login', methods=['POST',"GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('landing'))


@app.route('/dashboard')
def dashboard():
    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE students SET units = 'Complete' WHERE units = '120'")
    cursor.execute(f"UPDATE students SET status = 'Delayed' WHERE units != 'Complete' and year = '4th Year'")
    cursor.execute(f"UPDATE students SET status = 'Ongoing' WHERE units != '120' and year != '4th Year'")
    cursor.execute(f"UPDATE students SET status = 'Graduating' WHERE units = 'Complete'")
    mysql.connection.commit()
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM students ORDER BY name")
    students = cursor.fetchall()

    return render_template("dashboard.html", students=students)

@app.route('/add_students',methods=['POST','GET'])
def add_student():
    if request.method == "POST":
        ui_id = request.form.get('ui_id')
        name = request.form.get('fullname')
        age = request.form.get('age')
        section = request.form.get('section')
        year = request.form.get('year')
        major = request.form.get('major')
        units = request.form.get('units')
        status = request.form.get('status')
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO students (ui_id,name, age, year, section, major,units, status) Values ('{ui_id}','{name}','{age}','{year}','{section}','{major}','{units}','{status}')")
        mysql.connection.commit()
        return redirect('/dashboard')
    return render_template('add_students.html')

@app.route('/confirm/<string:id>', methods=["GET"])
def confirmation(id):
    print(id)
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM students WHERE ui_id = '{id}'")
    result = cursor.fetchone()
    cursor = mysql.connection.cursor()
    cursor.execute(f"INSERT INTO graduation_list (ui_id,name, age, year, section, major,units,status) Values ('{result[0]}','{result[1]}','{result[2]}','{result[3]}','{result[4]}','{result[5]}','{result[6]}','{result[7]}')")
    mysql.connection.commit()
    cursor.execute(f"DELETE FROM students WHERE ui_id = '{id}'")
    mysql.connection.commit()
    return redirect('/dashboard')


@app.route('/update/<string:id>',methods=["GET","POST"])
def delete(id):
    if request.method == "POST":
        fullname = request.form['fullname']
        age = request.form['age']
        year = request.form['year']
        section = request.form['section']
        major = request.form['major']
        units = request.form['units']
        status = request.form['status']
        cursor = mysql.connection.cursor()
        cursor.execute(f"UPDATE students SET ui_id = %s , name = %s, age = %s, year = %s, section = %s, major = %s, units = %s, status = %s WHERE ui_id = %s",(id,fullname, age, year, section, major, units, status, id))
        mysql.connection.commit()
        return redirect('/dashboard')
    else:

        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM students WHERE ui_id = '{id}'")
        result = cursor.fetchone()
        return render_template('update.html',result=result)

    

@app.route('/graduating_list')
def graduating():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Graduation_list ORDER BY name")
    students = cursor.fetchall()

    return render_template("graduating_list.html", students=students)


# main function
if __name__ == '__main__':
    app.run(debug=True)