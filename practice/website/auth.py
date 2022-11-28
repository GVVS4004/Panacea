from flask import Blueprint,flash, url_for,redirect
from flask import session
from flask import render_template
from flask import request,jsonify
from werkzeug.security import generate_password_hash ,check_password_hash
from website.models import User
from . import db
from flask_login import login_user,login_required,logout_user,current_user
from .views import home
auth =Blueprint('auth',__name__)

@auth.route('/login',methods=['POST','GET'])
def login():
    # Login_success=None
    if request.method=='POST':
        email = request.form["email"]
        password = request.form["password"]
        find_user = db.db.user.find_one({"email": email})
        if User.login_valid(email, password):
            loguser = User(find_user["firstname"],find_user["lastname"],find_user["email"],find_user["phno"],find_user["password"],find_user['_id'])
            login_user(loguser, remember=True)
            flash('You have been logged in!', 'success')
            return redirect(url_for('views.pie'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'error')
            return render_template('login.html',Login_success=False)
    return render_template('login.html',user=current_user ,Login_success=True)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/sign-up',methods=['POST','GET'])
def sign_up():
    if request.method=='POST':
        firstname = request.form["firstname"]
        lastname=request.form['lastname']
        email = request.form["email"]
        password1=request.form['password1']
        password2=request.form['password2']
        password = generate_password_hash(request.form["password1"])
        
        phno=request.form['phno']
        if len(email)<4 :
            flash('Email must be greater than 3 characters.',category='error')
        elif len(firstname)<2:
            flash(' First name should be greater than 1 character.', category='error')
        elif len(lastname)<2:
            flash(' Last name should be greater than 1 character.',category='error')
        elif password1!=password2:
            flash('Passwords do not match.', category='error')
        elif len(password1)<8:
            flash('password must be greater than 7 characters.', category='error')
        elif len(phno)<10 or len(phno)>10:
            flash('Mobile number should be 10 digits','error')
        else:
            find_user =  User.get_by_email(email)
            if find_user is None:
                User.register(firstname,lastname, email, password,phno)
                find_user = db.db.user.find_one({"email": email})
                loguser = User(find_user["firstname"],find_user["lastname"],find_user["email"],find_user["phno"],find_user["password"],find_user['_id'])
                login_user(loguser,remember=True)
                flash(f'Account created ', 'success')
                return redirect(url_for('views.pie'))
            else:
                flash(f'Account already exists', 'error')
    return render_template('registration.html',user=current_user)
































# @auth.route('/login',methods=['GET','POST'])
# def login():
#     if(request.method == 'POST'):
#         email=request.form.get('email')
#         logpassword=request.form.get('password')
#         # app,db=crete_app.create_app()
#         # db=crete_app.create_database()
#         from . import db
#         user1=User()
#         print(user1)
#         if user1:
#             if check_password_hash(user1['password'],logpassword) :
#                 print('success')
#                 flash('Logged in successfully!',category='success')
#                 login_user(user1,remember=True)
#                 return redirect(url_for('views.home'))
#             else:
#                 flash('Incorrect password,try again.',category='error')
#         else:
#             flash('Email doesnot exists.',category='error')
#     return render_template('login.html',boolean=True)

# @auth.route('/sign-up',methods=['GET','POST'])
# def sign_up():
#     if(request.method=='POST'):
#         email=request.form.get('email')
#         firstname =request.form.get('firstname')
#         lastname =request.form.get('lastname')
#         password1 =request.form.get('password1')
#         password2 =request.form.get('password2')
#         phno=request.form.get('phno')
#         # db=crete_app.create_database()
#         from . import db
#         from .models import User
#         if db.db.user.find_one({'email':email}):
#             flash('Email already exists.Please Login',category='error')
#         elif len(email)<4 :
#             flash('Email must be greater than 3 characters.',category='error')
#         elif len(firstname)<2:
#             flash(' First name should be greater than 1 character.', category='error')
#         elif len(lastname)<2:
#             flash(' Last name should be greater than 1 character.',category='error')
#         elif password1!=password2:
#             flash('password do not match.', category='error')
#         elif len(password1)<8:
#             flash('password must be greater than 7 characters.', category='error')
#         else:
#             hashpassword=generate_password_hash(password1,method='sha256')
#             user1=User.new_user(firstname,lastname,hashpassword,email,phno)
#             print(user1)
#             # db.db.user.insert_one({'_id':user1.user["_id"],
#             # 'fristname':firstname,
#             # 'lastname':lastname,
#             # 'email':email,
#             # 'password':user1.user['password'],
#             # 'mobile':phno,
#             # 'is_active':True,
#             # ''})
#             db.db.user.insert_one(user1)
#             flash('Account created', category='success')
#             login_user(user1,remember=True)
#             return redirect(url_for('views.home'))
#     return render_template("sign_up.html")