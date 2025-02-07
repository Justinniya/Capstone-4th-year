from flask import Flask,render_template,redirect,request,url_for
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'monitoring_database'

mysql = MySQL(app)
studentsss = [("John Doe", "20", "4th Year", "BSIT ", "Web Development ", "Graduating "),
            ("Jane Doe", "21", "3rd Year", "BSIT ", "Web Development ", "Graduating "),
            ("Juan Dela Cruz", "22", "2nd Year", "BSIT ", "Web Development ", "Graduating "),
            ("Juana Dela Cruz", "23", "1st Year", "BSIT ", "Web Development ", "Graduating ")]

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
        status = request.form.get('status')
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO students (ui_id,name, age, year, section, major, status) Values ('{ui_id}','{name}','{age}','{section}','{year}','{major}','{status}')")
        mysql.connection.commit()
        return redirect('/dashboard')
    return render_template('add_students.html')

@app.route('/confirm/<string:id>', methods=["GET"])
def confirmation(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE students SET confirmation = '1' WHERE ui_id = {id}")
    mysql.connection.commit()
    return redirect('/dashboard')


@app.route('/delete/<string:id>',methods=["GET"])
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM students WHERE ui_id = {id}")
    mysql.connection.commit()
    return redirect('/dashboard')


# main function
if __name__ == '__main__':
    app.run(debug=True)