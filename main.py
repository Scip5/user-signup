from flask import Flask, request, redirect, render_template
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def index():
    return render_template('user-signup.html')

@app.route("/signup", methods=["POST"])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    email_error = ""
    verify_error = ""

    if username == "":
        username_error = "Must enter username"
        username = ""
    
    if password == "":
        password_error = "Must enter a password"
        password = ""
        verify = ""
    
    if verify == "":
        verify_error = "Must enter matching password"
        password = ""
        verify = ""
    
    if password != verify:
        verify_error = "Passwords must match"
        password = ""
        verify = ""
    
    if len(username) < 2 or len(username) > 20:
        username_error =  "Not a valid username" 
        username = ""

    if len(email) >= 1:
        for char in email:
            if char == " ":
                email_error = "Not a valid email"
                break
    if len(email) >= 1:
        if "@" and "." not in email or len(email) < 2 or len(email) > 20:
                email_error = "Not a valid email"
                email = ""
    
    if username_error == "" and email_error == "" and password_error == "":
        return render_template('welcome_page.html', name=username)
    else:
        return render_template('user-signup.html', username=username, 
        username_error=username_error, password="", password_error=password_error,
        verify="", verify_error=verify_error, email=email, email_error=email_error )

app.run()