from flask import Flask, request, redirect, render_template, session, url_for
from sltTool import db

app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        session['username'] = request.form['email']
        print(session)
        return redirect(url_for('index'))


@app.route('/')
def index():
    print(session)
    if 'username' in session:
        username = session['username']
        return render_template("profile.html", username=username)
    else:
        return "You are not logged in <br><a href = 'user/login'>" + "click here to log in</a>"


@app.route('/user/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        email = request.values.get('email')
        password = request.values.get('password')
        db.create_user(email, password)
        return '<h2>' + email + ':' + password + " registered</h2>", 200


@app.route('/user/delete', methods=['GET', 'POST'])
def delete():
    if request.method == "GET":
        return render_template("delete.html")
    elif request.method == "POST":
        email = session["email"]
        password = request.values.get('password')
        db.delete_account(email, password)
        return '<h2>' + email + ':' + password + " deleted</h2>", 200


@app.route('/user/update/email', methods=['GET', 'POST'])
def update_email():
    if request.method == "GET":
        return render_template("update.html")
    elif request.method == "POST":
        email = session["email"]
        new_email = request.values.get('email')
        password = request.values.get('password')
        db.change_email(email, new_email, password)
        return '<h2>Email updated to ' + new_email + ': updated</h2>', 200


app.run(host='0.0.0.0', port=81, debug=True)