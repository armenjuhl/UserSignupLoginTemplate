from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user-signup:signup@localhost:8889/user-signup'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'aa687d6d70s8'

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
"""
@app.before_request
def require_login():
    allowed_routes = ['signup']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/')
"""


@app.route('/', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':            
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        verify_password = request.form['verify-password']
        # user = User.query.filter_by(username=username).first()
        # db.session.add.username()
        # db.session.add.password()
        # db.session.add.email()
        # db.session.commit()

        emailv = 0
        if len(username) < 3:
            flash('Username must be 3 characters or greater')
            return redirect('/')
        if password != verify_password:
            flash('Passwords must match')
            return redirect('/')
        if len(username) or len(password) or len(verify_password) or len(email) < 1:
            flash('You must complete the information from all fields')
            return redirect('/')
        for char in username or email or password:
            if char == " ":
                flash('Invalid character: You may not use a space')
                return redirect('/')
        for char in email:
            if char == '@':
                emailv = emailv +1
                if emailv < 1:
                    flash('Email must contain @ symbol')
                    return redirect('/')
        if len(username) or len(password) < 3 or len(username) or len(password) > 20:
            flash('Username and Password must be between 3-20 characters')
            return redirect('/')            
        else:
            session['username'] = username 
            #User.username = User.query.filter_by(username=session['username']).first()
            flash("Welcome", + username)
            return redirect('/welcome')

        #if user and user.password == password:
            #session['username'] = username
            #return redirect('/')
        #else:
            #return '<h1>Error!</h1>'

        
    flash('welcome')  
    return render_template('signup.html')

@app.route('/welcome', methods=['POST', 'GET'])
def welcomePage():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run()
