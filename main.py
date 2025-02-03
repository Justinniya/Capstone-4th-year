from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)

students = [("John Doe", "20", "4th Year", "BSIT ", "Web Development ", "Graduating "),
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
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", students=students)


if __name__ == '__main__':
    app.run(debug=True)