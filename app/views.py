from app import *
from flask import render_template, request
from app.forms import ContactForm
from flask_sqlalchemy import SQLAlchemy
from .models import  User


@app.route("/")
def index():
    user_data = User.query.all()
    return  render_template('home.html', users=user_data)

@app.route("/register", methods=["GET", "POST"])
def register():
    #check the request method to ensure the handling of POST request only
    if request.method == "POST":
        #store the form value
        user_name = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        useer = User(username= user_name, user_email = email, user_password = password )
        db.session.add(useer)
        db.session.commit()
        return user_name + " <br/> " + email
    return render_template('register.html')


@app.route('/deletauser/<int:pk>', methods=["GET","DELETE" "POST" ])
def delete_user(pk):
    user = User.query.get_or_404(pk)
    db.session.delete(user)
    db.session.commit()
    return 'user deleted successfully'





@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        return name + "<br /> " + email + "<br /> " + message

    return render_template('contact.html', form=form)