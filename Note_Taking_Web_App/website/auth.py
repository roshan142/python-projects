from flask import Blueprint , render_template , request , flash, redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint("auth",__name__)
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user= User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("Logged In Successfully!", category="success")
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password, try again.", category="error")
        else:
            flash("Email Does not Exist.", category='error')

    return render_template("login.html", user=current_user)
@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user= User.query.filter_by(email=email).first()
        if user:
            flash("This Email Already Exists.", category='error')
        elif len(email) <4:
            flash("Email Must be greater than 3 char", category="error")
        elif len(first_name) <2:
            flash("First Name Must be greater than 2 char", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        elif len(password1) < 6:
            flash("password must be greater than 6", category="error")
        else:
            new_user = User(email = email, first_name= first_name,password= generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account has been created successfully", category="success")
            login_user(new_user,remember=True)
            return redirect(url_for('views.home'))
    return render_template("sign_up.html",user=current_user)
@auth.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('auth.login'))