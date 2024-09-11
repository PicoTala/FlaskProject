from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

# create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key of some kind"

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