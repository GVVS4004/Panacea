from flask import Blueprint
from flask import render_template
from flask_login import login_required,current_user
views =Blueprint('views',__name__)
from . import db
@views.route('/')
@login_required
def home():
    user=db.db.user.find_one({'firstname':'Shashi'})
    print(user)
    months={'detail1':{
        'carbohydrates':20,
        'fats':30,
        'protiens':15,
        'vitamins':10,
        'calories':20,
        'sugars':5
    },
    'detail2':{
        'carbohydrates':10,
        'fats':10,
        'protiens':20,
        'vitamins':20,
        'calories':30,
        'sugars':10
    }}
    lis=list()
    i=0
    j=0
    for month in months:
        templis=list()
        for value in months[month].values():
            templis.append(value)
            
        lis.append(templis)
    print(lis)
    return render_template('home.html',user=current_user,lis=lis,len=2)
