from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create a Flask instance
app = Flask(__name__)

# Add Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'

# Secret Key
app.config['SECRET_KEY'] = "secret key of some kind"

# Initialize the Database
# db = SQLAlchemy(app)

# Create Model

# class Inventory(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(200), nullable=False)
    # collection = db.Column(db.String(200), nullable=True)
    # item_type = db.Column(db.String(200), nullable=True)
    # description = db.Column(db.String(400), nullable=True)
    # purchase_price = db.Column(db.Float, nullable=True)
    # appraisal_amount = db.Column(db.Float, nullable=True)
    # date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a string
    # def __repr__(self):
        # return '<Name %r>' % self.name

# create a route decorator
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/blogging')
def blogging():
    return render_template("blogging.html")

@app.route('/designing')
def designing():
    return render_template("designing.html")

@app.route('/working')
def working():
    return render_template("working.html")

@app.route('/chatting', methods=['GET', 'POST'])
def chatting():
    form = ContactForm()
    return render_template("chatting.html", form = form)

# routing for subpages (may alter this)

@app.route('/adventing')
def adventing():
    return render_template("/post/adventing.html")

@app.route('/resume_article')
def resume_article():
    return render_template("/post/resume_article.html")

@app.route('/cat_breakfast')
def cat_breakfast():
    return render_template("/post/The_Cat_Wants_Breakfast.html")

@app.route('/apple_dumplings')
def apple_dumplings():
    return render_template("/post/appledumplings.html")

@app.route('/cross_stitch_download')
def cross_stitch_download():
    return render_template("/post/stitching.html")

@app.route('/stuffed_peppers')
def stuffed_peppers():
    return render_template("/post/stuffedpeppers.html")

@app.route('/ramen_writeup')
def ramen_writeup():
    return render_template("/post/ramenwriteup.html")

# create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create a Form Class
class ContactForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    email = StringField("What's your email?", validators=[Email()])
    message = TextAreaField("Leave your message here.", validators=[DataRequired()])
    submit = SubmitField("Submit")