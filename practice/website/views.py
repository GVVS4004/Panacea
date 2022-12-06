import json
from flask import Blueprint,jsonify
from flask import render_template,url_for,request,redirect,session
from flask_login import login_required,current_user
import boto3
import sys,os
import re
import json
from collections import defaultdict
import requests,os,pprint
import spoonacular as sp
api = sp.API("b8cf3af47090431c8648f42c61944428")
views =Blueprint('views',__name__)
import json
from . import db


#HOME
@views.route('/')
def home():
    return render_template('home.html')
@views.route('/items',methods=['POST','GET'])
def items():
    return render_template("index.html")

# USER DASH_BOARD
@views.route('/pie')
@login_required
def pie():
    uid=current_user._id
    lis=list()
    len1=list()
    mnts=list()
    years=list()
    lis1=db.db.nutrition_info.find_one({'uid':uid})
    firstmonth=None
    firstyear=None
    if lis1!=None:
        i=0
        for year in lis1['years']:
            if(i==0):
                firstyear=year
        lis=lis1['years']

        i=0
        for month in lis[firstyear]:
            if(i==0):
                firstmonth=month
        print(lis)
    bl=False
    if len(lis)!=0:
        bl=True
    return render_template('dashboard.html',user=current_user,res=lis,bl=bl,firstmonth=firstmonth,firstyear=firstyear)



@views.route("/base")
def base():
    return render_template('dash_base.html')
# @views.route('/item/<name>')
# def item(name):
#     import requests

#     url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

#     querystring = {"ingr":str(name)}

#     headers = {
#         "X-RapidAPI-Key": "4851f7cfd4mshd48600fa805a277p1dc4b1jsn088a52e2e286",
#         "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     # pprint.pprint(response.json(),indent=4)
#     data=response.json()
#     length=len(data['hints'])
#     items=[]
#     foodids=[]
#     i=0
#     for i in range(length):
#         temp={}
#         temp['label']=data['hints'][i]['food']['label']
#         if data['hints'][i]['food']['foodId'] not in foodids:
#             try :
#                 temp['cal']=round(float(data['hints'][i]['food']['nutrients']['ENERC_KCAL']),2)
#             except:
#                 temp['cal']=None
#             try :
#                 temp['carbs']=round(float(data['hints'][i]['food']['nutrients']['CHOCDF']),2)
#             except :
#                 temp['carbs']=None
#             try :
#                 temp['fats']=round(float(data['hints'][i]['food']['nutrients']['FAT']),2)
#             except:
#                 temp['fats']=None
#             try:
#                 temp['fib']=round(float(data['hints'][i]['food']['nutrients']['FIBTG']),2)
#             except:
#                 temp['fib']=None
#             try:
#                 temp['pro']=round(float(data['hints'][i]['food']['nutrients']['PROCNT']),2)
#             except:
#                 temp['pro']=None
#             try:
#                 temp['src']=data['hints'][i]['food']['image']
#             except:
#                 temp['src']=None
#             try:
#                 temp['food_id']=data['hints'][i]['food']['foodId']
#                 foodids.append(data['hints'][i]['food']['foodId'])
#             except:
#                 temp['food_id']=None
#             items.append(temp)
#     return render_template('item.html',items=items,name=name)

#---------------------------------------------------------------FOOD INFO ROUTE------------------------------------------------------
#MAKE CHANGES HERE

@views.route('/<name>/info')
def info(name):
    # url = 'https://api.spoonacular.com/food/products/search?apiKey=b8cf3af47090431c8648f42c61944428&query={name}'
    response = api.parse_ingredients(str(name))
    data = response.json()
    quant=data[0]['amount']
    srcunit=data[0]['unit']
    nutrition=data[0]['nutrition']['nutrients']
    name1=data[0]['name']
    spoonacular_api_url=requests.get(url)
    convert_url='https://api.spoonacular.com/recipes/convert?apiKey=b8cf3af47090431c8648f42c61944428&ingredientName=uraddal&sourceAmount='+str(quant)+'&sourceUnit='+srcunit+'&targetUnit=grams'
    spoonacular_api_convert_url=requests.get(convert_url)
    amt=spoonacular_api_convert_url.json()
    amount=amt['targetAmount']
    result=spoonacular_api_url.json()
    # pprint.pprint(result)
    # print(result['products'][1]['image'])
    print(name1)
    print(amount)
    pprint.pprint(nutrition)
    return render_template('')

#----------------------------------------------------ADDING ITEMS TO THE USERS CART--------------------------------------------------------
@views.route("/addcart/<food_id>",methods=['POST'])
def addcart(food_id):
    food_name=request.form.get('foodname'+str(food_id))
    if request.method=='POST':
        food_wt=request.form.get('wt')
        food_name=request.form.get('foodname'+str(food_id))
        food_info={request.form.get('foodinfo'+str(food_id))}
        print('foodname'+str(food_id))
        print(((food_info)))
        url='/item/'+str(food_name)
        # print(url)
        uid=current_user._id
        if db.db.carts.find_one({'uid':uid}):
            # print(db.db.carts.find_one({'uid':uid}))
            import spoonacular as sp
            api = sp.API("b8cf3af47090431c8648f42c61944428")
            temp_response=api.parse_ingredients(food_name)
            data = temp_response.json()
            src='https://spoonacular.com/cdn/ingredients_100x100/'+str(data[0]['image'])
            nutrition=data[0]['nutrition']
            quant=data[0]['amount']
            srcunit=data[0]['unit']
            cnvrt_amt=api.convert_amounts(food_name,'gram',quant,srcunit)
            cnvrt_amt=cnvrt_amt.json()['targetAmount']
            items=db.db.carts.find_one({'uid':uid})
            items=items['food_items']
            itemslen=len(items)
            items[str(food_id)]={'_id':str(food_id),'food_name':food_name,'quant':food_wt,'convert_amt':cnvrt_amt,'src':src,'nutrition':nutrition}
            db.db.carts.update_one({'uid':uid},{"$set":{'food_items':items}})
            # db.db.carts.insert_one({'uid':uid,'food_items':{'food_id':food_id,'food_name':food_name,'quant':food_wt}})
        else:
            import spoonacular as sp
            api = sp.API("b8cf3af47090431c8648f42c61944428")
            temp_response=api.parse_ingredients(food_name)
            data = temp_response.json()
            src='https://spoonacular.com/cdn/ingredients_100x100/'+str(data[0]['image'])
            nutrition=data[0]['nutrition']
            quant=data[0]['amount']
            srcunit=data[0]['unit']
            cnvrt_amt=api.convert_amounts(food_name,'gram',quant,srcunit)
            cnvrt_amt=cnvrt_amt.json()['targetAmount']
            db.db.carts.insert_one({'uid':uid,'food_items':{str(food_id):{'_id':str(food_id),'food_name':food_name,'quant':food_wt,'convert_amt':cnvrt_amt,'src':src,'nutrition':nutrition}}})


        return redirect(url)
    url='/item/'+str(food_name)
    print(url)
    return redirect(url)
# @views.route('/cart',methods=['POST','GET'])
# def cart():
#     uid=current_user._id
#     cur_user_items=db.db.carts.find_one({'uid':uid})['food_items']
#     print(cur_user_items)
#     items=[]
#     for j in cur_user_items:
#         cur_food_id=cur_user_items[str(j)]['food_id']
#         cur_food_name=cur_user_items[str(j)]['food_name']
#         cur_food_wt=cur_user_items[str(j)]['quant']
#         import requests

#         url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

#         querystring = {"ingr":str(cur_food_name)}

#         headers = {
#             "X-RapidAPI-Key": "4851f7cfd4mshd48600fa805a277p1dc4b1jsn088a52e2e286",
#             "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
#         }

#         response = requests.request("GET", url, headers=headers, params=querystring)
#         data=response.json()
#         print('hints:::::::::')
#         pprint.pprint(data['hints'])
#         length=len(data['hints'])
#         for i in range(length):
#             if cur_food_id==data['hints'][i]['food']['foodId']:
#                 temp={}
#                 temp['label']=data['hints'][i]['food']['label']
#                 try :
#                     temp['cal']=round(float(data['hints'][i]['food']['nutrients']['ENERC_KCAL']),2)
#                 except:
#                     temp['cal']=None
#                 try :
#                     temp['carbs']=round(float(data['hints'][i]['food']['nutrients']['CHOCDF']),2)
#                 except :
#                     temp['carbs']=None
#                 try :
#                     temp['fats']=round(float(data['hints'][i]['food']['nutrients']['FAT']),2)
#                 except:
#                     temp['fats']=None
#                 try:
#                     temp['fib']=round(float(data['hints'][i]['food']['nutrients']['FIBTG']),2)
#                 except:
#                     temp['fib']=None
#                 try:
#                     temp['pro']=round(float(data['hints'][i]['food']['nutrients']['PROCNT']),2)
#                 except:
#                     temp['pro']=None
#                 try:
#                     temp['src']=data['hints'][i]['food']['image']
#                 except:
#                     temp['src']=None
#                 try:
#                     temp['food_id']=data['hints'][i]['food']['foodId']
#                     # foodids.append(data['hints'][i]['food']['foodId'])
#                 except:
#                     temp['food_id']=None
#                 temp['wt']=cur_food_wt
#                 items.append(temp)

#     return render_template('cart.html',items=items)

#------------------------------------------------------SEARCHING A PARTICULAR ITEM AND IT'S NUTRITIONAL VALUES-------------------------------------

@views.route('/item/<name>')
def item(name):
    # autocomplete_url='https://api.spoonacular.com/food/ingredients/autocomplete?apiKey=b8cf3af47090431c8648f42c61944428&query={name}'
    # autocomplete_results=requests.get(autocomplete_url)
    try:
        autocomplete_result=api.autocomplete_ingredient_search(name,number=5)
        autocomplete_results=autocomplete_result.json()
        pprint.pprint(autocomplete_results)
    
        # autocomplete_name=autocomplete_results[0]['name']
        # autocomplete_name=name
        autocomplete_items=list()
    
        # for item in range(len(autocomplete_results)):
        for i in range(len(autocomplete_results)):
            temp={}
            # temp['name']=name
            # temp['name']=autocomplete_results[item]['name']
            # temp['src']='https://spoonacular.com/cdn/ingredients_100x100/'+str(autocomplete_results[item]['image'])
            autocomplete_name=autocomplete_results[i]['name']
            # temp['food_id']=autocomplete_results['id']
            temp_response=api.parse_ingredients(autocomplete_name)
            data = temp_response.json()
            quant=data[0]['amount']
            srcunit=data[0]['unit']
            temp['food_id']=data[0]['id']
            temp['src']='https://spoonacular.com/cdn/ingredients_100x100/'+str(data[0]['image'])
            temp['name']=data[0]['name']
            nutrition=data[0]['nutrition']
            cnvrt_amt=api.convert_amounts(temp['name'],'gram',quant,srcunit)
            cnvrt_amt=cnvrt_amt.json()['targetAmount']
            print(cnvrt_amt)
            nutrients=(data[0]['nutrition']['nutrients'])
            for nutrient in nutrients:
                if nutrient['name']=='Fat':
                    temp['fats']=round(((nutrient['amount'])*100)/float(cnvrt_amt),0)
                elif nutrient['name']=='Protein':
                    temp['pro']=round(((nutrient['amount'])*100)/float(cnvrt_amt),0)
                elif nutrient['name']=='Carbohydrates':
                    temp['carbs']=round(((nutrient['amount'])*100)/float(cnvrt_amt),)
                elif nutrient['name']=='Calories':
                    temp['cal']=round(((nutrient['amount'])*100)/float(cnvrt_amt),0)
                elif nutrient['name']=='Sugar':
                    temp['sug']=round(((nutrient['amount'])*100)/float(cnvrt_amt),0)
            temp['nutrition']=nutrition
            autocomplete_items.append(temp)
    except:
        return render_template('item.html',error=True)
    return render_template('item.html',items=autocomplete_items,error=False)

#---------------------------------------DISPLAYING THE ITEMS IN USER'S CART-----------------------------------------

@views.route('/cart',methods=['POST','GET'])
def cart(upload=False):
    uid=current_user._id
    empty=False
    items=[]
    

    if db.db.carts.find_one({'uid':uid}):
        cur_user_items=db.db.carts.find_one({'uid':uid})['food_items']
        # print(cur_user_items)
        
        for j in cur_user_items:
            temp={}
            cur_food_id=j
            cur_food_name=cur_user_items[str(j)]['food_name']
            cur_food_wt=cur_user_items[str(j)]['quant']
            cur_food_src=cur_user_items[str(j)]['src']
            cnvrt_amt=cur_user_items[str(j)]['convert_amt']
            nutrients=(cur_user_items[str(j)]['nutrition']['nutrients'])
            print(j)
            for nutrient in nutrients:
                if nutrient['name']=='Fat':
                    temp['fats']=int(round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),0))
                elif nutrient['name']=='Protein':
                    temp['pro']=int(round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),0))
                elif nutrient['name']=='Carbohydrates':
                    temp['carbs']=int(round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),0))
                elif nutrient['name']=='Calories':
                    temp['cal']=int(round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),0))
                elif nutrient['name']=='Sugar':
                    temp['sug']=int(round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),0))
            temp['food_id']=cur_food_id
            temp['food_name']=cur_food_name
            temp['food_wt']=cur_food_wt
            temp['src']=cur_food_src
            items.append(temp)
            print(len(items))
            if len(items)==0:
                empty=True
    if len(items)==0:
        empty=True
    msg=False
    
    upload=request.args.get(upload)
    if upload==True:
        msg=True
    print(upload)
    return render_template('cart.html',items=items,empty=empty,msg=msg)

#------------------------------------------------DELETING THE ITEM'S IN THE CART------------------------------------------------

@views.route('/delete/<food_id>',methods=['POST'])
def item_delete(food_id):
    
    uid=current_user._id
    db.db.carts.update_one({'uid':uid},{'$unset': {"food_items."+str(food_id):{'_id': food_id}}})
    # print(db.db.carts.find_one({'uid':uid})['food_items'][str(food_id)])
    # db.db.carts.__find_and_modify()
    return redirect(url_for('views.cart'))

@views.route('/analyse', methods=['POST'])
def analysis():
    if request.method=="POST":
        cur_month=request.form.get('month')
        cur_year=request.form.get('year')
        done=True
        uid=current_user._id
        cur_user_items=db.db.carts.find_one({'uid':uid})['food_items']
        items=[]
        info={'pro':float(0),'fats':float(0),'carbs':float(0),'sug':float(0),'cal':float(0)}
        for j in cur_user_items:
            temp={}
            cur_food_id=j
            cur_food_name=cur_user_items[str(j)]['food_name']
            cur_food_wt=cur_user_items[str(j)]['quant']
            cur_food_src=cur_user_items[str(j)]['src']
            cnvrt_amt=cur_user_items[str(j)]['convert_amt']
            nutrients=(cur_user_items[str(j)]['nutrition']['nutrients'])
            for nutrient in nutrients:
                if nutrient['name']=='Fat':
                    temp['fats']=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                    info['fats']+=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                elif nutrient['name']=='Protein':
                    temp['pro']=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                    info['pro']+=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                elif nutrient['name']=='Carbohydrates':
                    temp['carbs']=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                    info['carbs']+=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                elif nutrient['name']=='Calories':
                    temp['cal']=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                    info['cal']+=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                elif nutrient['name']=='Sugar':
                    temp['sug']=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
                    info['sug']+=round(((nutrient['amount'])*float(cur_food_wt))/float(cnvrt_amt),3)
            temp['food_id']=cur_food_id
            temp['food_name']=cur_food_name
            temp['food_wt']=cur_food_wt
            temp['src']=cur_food_src
            items.append(temp)
        cur_month_nutri_info=info
        if db.db.nutrition_info.find_one({'uid':uid}):
            try:
                print("try")
                years=db.db.nutrition_info.find_one({'uid':uid})['years']
                years[cur_year][str(cur_month)]=cur_month_nutri_info
                db.db.nutrition_info.update_one({'uid':uid},{"$set":{'years':years}})
            except:
                print("except")
                years=db.db.nutrition_info.find_one({'uid':uid})['years']
                tempdict={cur_month:cur_month_nutri_info}
                years[cur_year]=tempdict
                db.db.nutrition_info.update_one({'uid':uid},{"$set":{'years':years}})
        else:
            db.db.nutrition_info.insert_one({'uid':uid,"years":{cur_year:{(cur_month):cur_month_nutri_info}}})
        db.db.carts.find_one_and_delete({'uid':uid})
    return redirect(url_for('views.pie'))

#------------------------------------------CREATING A AWS TEXTRACT CLASS-----------------------------------------------------

class texTract:
        def get_kv_map(file_name):
            with open(os.path.join(os.path.dirname(__file__),'static/image_uploads/'+file_name), 'rb') as file:
                img_test = file.read()
                bytes_test = bytearray(img_test)
                print('Image loaded', file_name)

            client = boto3.client('textract', region_name="", aws_access_key_id='',aws_secret_access_key= '')
            response = client.analyze_document(Document={'Bytes': bytes_test,
            'S3Object':{
                'Bucket':"penaceatextract",
            }}, FeatureTypes=['FORMS'])

            blocks = response['Blocks']
            key_map = {}
            value_map = {}
            block_map = {}
            for block in blocks:
                block_id = block['Id']
                block_map[block_id] = block
                if block['BlockType'] == "KEY_VALUE_SET":
                    if 'KEY' in block['EntityTypes']:
                        key_map[block_id] = block
                    else:
                        value_map[block_id] = block

            return key_map, value_map, block_map


        def get_kv_relationship(key_map, value_map, block_map):
            kvs = defaultdict(list)
            for block_id, key_block in key_map.items():
                value_block = texTract.find_value_block(key_block, value_map)
                key = texTract.get_text(key_block, block_map)
                val = texTract.get_text(value_block, block_map)
                kvs[key].append(val)
            return kvs


        def find_value_block(key_block, value_map):
            for relationship in key_block['Relationships']:
                if relationship['Type'] == 'VALUE':
                    for value_id in relationship['Ids']:
                        value_block = value_map[value_id]
            return value_block


        def get_text(result, blocks_map):
            text = ''
            if 'Relationships' in result:
                for relationship in result['Relationships']:
                    if relationship['Type'] == 'CHILD':
                        for child_id in relationship['Ids']:
                            word = blocks_map[child_id]
                            if word['BlockType'] == 'WORD':
                                text += word['Text'] + ' '
                            if word['BlockType'] == 'SELECTION_ELEMENT':
                                if word['SelectionStatus'] == 'SELECTED':
                                    text += 'X '

            return text


        def print_kvs(kvs):
            for key, value in kvs.items():
                print(key, ":", int(value[0]))


        def search_value(kvs, search_key):
            for key, value in kvs.items():
                if re.search(search_key, key, re.IGNORECASE):
                    return value


        def main(file_name):
            key_map, value_map, block_map = texTract.get_kv_map(file_name)

            # Get Key Value relationship
            kvs = texTract.get_kv_relationship(key_map, value_map, block_map)
            print("\n\n== FOUND KEY : VALUE pairs ===\n")
            texTract.print_kvs(kvs)


            # Start searching a key value
            # while input('\n Do you want to search a value for a key? (enter "n" for exit) ') != 'n':
            #     search_key = input('\n Enter a search key:')
            #     print('The value is:', search_value(kvs, search_key))
            uid=current_user._id
            for key,value in kvs.items(): 
                if db.db.carts.find_one({'uid':uid}):
                    try:
                        temp_response=api.parse_ingredients(key)
                        data = temp_response.json()
                        src='https://spoonacular.com/cdn/ingredients_100x100/'+str(data[0]['image'])
                        nutrition=data[0]['nutrition']
                        quant=data[0]['amount']
                        srcunit=data[0]['unit']
                        food_id=data[0]['id']
                        cnvrt_amt=api.convert_amounts(key,'gram',quant,srcunit)
                        cnvrt_amt=cnvrt_amt.json()['targetAmount']
                        items=db.db.carts.find_one({'uid':uid})
                        items=items['food_items']
                        itemslen=len(items)
                        items[str(food_id)]={'_id':str(food_id),'food_name':key,'quant':int(value[0]),'convert_amt':cnvrt_amt,'src':src,'nutrition':nutrition}
                        db.db.carts.update_one({'uid':uid},{"$set":{'food_items':items}})
                    except:
                        pass
                    # db.db.carts.insert_one({'uid':uid,'food_items':{'food_id':food_id,'food_name':food_name,'quant':food_wt}})
                else:
                    try:
                        temp_response=api.parse_ingredients(key)
                        data = temp_response.json()
                        src='https://spoonacular.com/cdn/ingredients_100x100/'+str(data[0]['image'])
                        nutrition=data[0]['nutrition']
                        quant=data[0]['amount']
                        srcunit=data[0]['unit']
                        food_id=data[0]['id']
                        cnvrt_amt=api.convert_amounts(key,'gram',quant,srcunit)
                        cnvrt_amt=cnvrt_amt.json()['targetAmount']
                        db.db.carts.insert_one({'uid':uid,'food_items':{str(food_id):{'_id':str(food_id),'food_name':key,'quant':int(value[0]),'convert_amt':cnvrt_amt,'src':src,'nutrition':nutrition}}})
                    except:
                        pass
            print('main end')

#----------------------------------------------------------UPLOADING THE ITEMS FROM A DOCUMENT---------------------------------------------

@views.route('/upload',methods=['POST','GET'])
def upload():
    if request.method=='POST':
        

        file_name=request.files.get('file')
        file_name.save(os.path.join(os.path.dirname(__file__),'static/image_uploads/'+file_name.filename))
        try :
            texTract.main(file_name.filename)
            return redirect(url_for('views.cart',upload=True))
        except:
            return render_template('uploadfile.html',err=True)

    return render_template('uploadfile.html',err=False)
