from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'ThisismyDB'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/kellylin/flask/users.db"

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15))
    email = db.Column(db.String(50))
    password = db.Column(db.String(20))
    name = db.Column(db.String(50))
    

@app.route('/home', methods=['GET', 'POST'])
def home():
    return "hello world"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_user = Users(username = request.form['username'], email = request.form['email'], password = request.form['password'], name = request.form['name'])
        db.session.add(new_user)
        db.session.commit()
        return redirect('/home')
    return render_template('signup.html')

@app.route('/getusers')
def getusers():
    all_users = Users.query.all()
    return render_template('getusers.html', user=all_users)


if __name__ == '__main__':
    app.run(debug=True)
    