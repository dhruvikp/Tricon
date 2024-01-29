from flask import Flask, render_template, request,redirect,url_for, session, flash, jsonify
import logging


app = Flask(__name__)
app.secret_key = 'mysecretkey'
# app.logger.setLevel(logging.INFO)

@app.route("/fancy")
def hello_world():
    data = {'name':'Dhruvik', "age":34}
    return jsonify(data)

@app.route("/fancy1")
def hello_world1():
    name="Alex Simplilearn"
    template_name = "Jinja2"

    movies= [
        "movie1",
        "movie2",
        "movie3"
    ]

    cars = {
        "brand":"Tesla",
        "model":"Roadster",
        "Year":2023
    }

    kwargs = {
        "name": name,
        "template_name": template_name,
        "movies": movies,
        "cars":cars,
        "company":"Dell"
    }

    return render_template("jinja_intro.html", **kwargs)


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login-submit", methods=["post"])
def loginSubmit():
    username = request.form.get("username")
    password = request.form.get("password")

    if username== 'admin' and password == 'admin':
        flash('Login successful')
        session['logged_in_user']='admin'
        return redirect(url_for('dashboard')) 
    else:
        return render_template("login.html", error =True)

@app.route("/dashboard")
def dashboard():
    
    if 'logged_in_user' in session and session['logged_in_user']:
        username = session['logged_in_user']
    else:
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=username)

@app.route("/logout")
def logout():
    flash('you have been logged out')
    session.pop('logged_in_user',None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)