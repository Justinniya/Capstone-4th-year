from flask import Flask,render_template,redirect,request,url_for,session,flash
from flask_mysqldb import MySQL

# Paghimo sang Flask app
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # Host sang MySQL database
app.config['MYSQL_USER'] = 'root'  # User sang database
app.config['MYSQL_PASSWORD'] = ''  # Password sang database (wala ini sa default localhost)
app.config['MYSQL_DB'] = 'monitoring_database'  # Ngalan sang database
app.secret_key = "monitoring"  # Secret key para sa session management

mysql = MySQL(app)  # Pag-initialize sang MySQL

# Route para sa landing page
@app.route('/')
def landing():
    return render_template("landing.html")

# Route para sa login page
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':  # Hardcoded login credentials
            session['logged'] = username  # Pag-store sang session
            flash('Login successful!', 'success')  # Flash message kung success
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'danger')  # Error message kung failed
            return redirect(url_for('landing'))

# Route para sa dashboard
@app.route('/dashboard')
def dashboard():
    logged = session.get('logged')  # Pagkuha sang session kung nakalog-in
    if logged:
        cursor = mysql.connection.cursor()
        # Pag-update sang status sang students depende sa ila units
        cursor.execute("UPDATE students SET units = 'Complete' WHERE units = '120'")
        cursor.execute("UPDATE students SET status = 'Delayed' WHERE units != 'Complete' and year = '4th Year'")
        cursor.execute("UPDATE students SET status = 'Ongoing' WHERE units != '120' and year != '4th Year'")
        cursor.execute("UPDATE students SET status = 'Graduating' WHERE units = 'Complete'")
        mysql.connection.commit()
        
        # Pagkuha sang tanan nga students kag pag-sort sang ila ngalan
        cursor.execute("SELECT * FROM students ORDER BY name")
        students = cursor.fetchall()
        
        return render_template("dashboard.html", students=students, page="dashboard")
    else:
        return redirect('/')  # Kung wala nakalog-in, ibalik sa landing page

# Route para sa pagdugang sang estudyante
@app.route('/add_students',methods=['POST','GET'])
def add_student():
    logged = session.get('logged')
    if logged:
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
        return render_template('add_students.html' ,page="add_students")
    else:
        return redirect('/')

# Route para sa pag-confirm sang graduation
@app.route('/confirm/<string:id>', methods=["GET"])
def confirmation(id):
    logged = session.get('logged')
    if logged:
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM students WHERE ui_id = '{id}'")
        result = cursor.fetchone()
        cursor.execute(f"INSERT INTO graduation_list (ui_id,name, age, year, section, major,units,status) Values ('{result[0]}','{result[1]}','{result[2]}','{result[3]}','{result[4]}','{result[5]}','{result[6]}','{result[7]}')")
        mysql.connection.commit()
        cursor.execute(f"DELETE FROM students WHERE ui_id = '{id}'")  # Pag-delete sang student sa list
        mysql.connection.commit()
        return redirect('/dashboard')
    else:
        return redirect('/')

# Route para sa pag-update sang student info
@app.route('/update/<string:id>',methods=["GET","POST"])
def delete(id):
    logged = session.get('logged')
    if logged:
        if request.method == "POST":
            fullname = request.form['fullname']
            age = request.form['age']
            year = request.form['year']
            section = request.form['section']
            major = request.form['major']
            units = request.form['units']
            status = request.form['status']
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE students SET ui_id = %s , name = %s, age = %s, year = %s, section = %s, major = %s, units = %s, status = %s WHERE ui_id = %s",(id,fullname, age, year, section, major, units, status, id))
            mysql.connection.commit()
            return redirect('/dashboard')
        else:
            cursor = mysql.connection.cursor()
            cursor.execute(f"SELECT * FROM students WHERE ui_id = '{id}'")
            result = cursor.fetchone()
            return render_template('update.html',result=result)
    else:
        return redirect('/')

# Route para sa graduating students list
@app.route('/graduating_list')
def graduating():
    logged = session.get('logged')
    if logged:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Graduation_list ORDER BY name")
        students = cursor.fetchall()
        return render_template("graduating_list.html", students=students, page="graduating_list")
    else:
        return redirect('/')

# Main function para mag-run sang Flask app
if __name__ == '__main__':
    app.run(debug=True)
