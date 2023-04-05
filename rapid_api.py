# # import requests,pprint

# # url = "https://nutritionix-api.p.rapidapi.com/v1_1/search/cheddar%20cheese"

# # querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_total_fat"}

# # headers = {
# # 	"X-RapidAPI-Key": "4851f7cfd4mshd48600fa805a277p1dc4b1jsn088a52e2e286",
# # 	"X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com"
# # }

# # response = requests.request("GET", url, headers=headers, params=querystring)

# # pprint.pprint(response.text)


# import requests,os,pprint
# import spoonacular as sp
# os.environ['spoonacular_api_key']="b8cf3af47090431c8648f42c61944428"
# spoonacular_api_key =os.environ["spoonacular_api_key"]
# print(spoonacular_api_key)

# url = 'https://api.spoonacular.com/food/products/search?apiKey=b8cf3af47090431c8648f42c61944428&query=apple'
# nutri_url='https://api.spoonacular.com/recipes/parseIngredients?apiKey=b8cf3af47090431c8648f42c61944428&ingredientList=urad dal'
# api = sp.API("b8cf3af47090431c8648f42c61944428")

# Parse an ingredient
# nutrition='nutrition'
# response = api.parse_ingredients("moong dal")
# print(response)
# data = response.json()
# pprint.pprint(data)
# quant=data[0]['amount']
# srcunit=data[0]['unit']
# nutrition=data[0]['nutrition']['nutrients']
# pprint.pprint(data)
# image=data[0]['image']
# print('https://spoonacular.com/cdn/ingredients_100x100/'+str(image))



# spoonacular_api_url=requests.get(url)
# spoonacular_api_nutri_url=requests.get(nutri_url).json()
# # spoonacular_api_convert_url=requests.get(convert_url).json()
# image=spoonacular_api_url[0]['image']
# nutrition=spoonacular_api_nutri_url[0]['nutrition']['nutrients']
# quant=spoonacular_api_nutri_url[0]['amount']
# srcunit=spoonacular_api_nutri_url[0]['unit']
# convert_url='https://api.spoonacular.com/recipes/convert?apiKey=b8cf3af47090431c8648f42c61944428&ingredientName=uraddal&sourceAmount='+str(quant)+'&sourceUnit='+srcunit+'&targetUnit=grams'
# print(convert_url)
# spoonacular_api_convert_url=requests.get(convert_url)
# amt=spoonacular_api_convert_url.json()
# amount=amt['targetAmount']
# print(image)
# print(nutrition)
# print(amount)

# print(spoonacular_api_url)
# result=spoonacular_api_url.json()
# pprint.pprint(result)
# print(result['products'][1]['image'])
# print(amount)
# print(nutrition)


# import requests

# def getRecipeByIngredients(ingredients):
#     payload = {
#         'fillIngredients': False,
#         'ingredients': ingredients,
#         'limitLicense': False,
#         'number': 5,
#         'ranking': 1
#     }

#     api_key = "b8cf3af47090431c8648f42c61944428"

#     endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients"


#     headers={
#         "X-Mashape-Key": api_key,
#         "X-Mashape-Host": "mashape host"
#     }

#     r = requests.get(endpoint, params=payload, headers=headers)
#     results = r.json()
#     title = results[0]['title']
#     print(title)

# getRecipeByIngredients('apple')
# import requests

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

# querystring = {"query":"pasta","cuisine":"italian","excludeCuisine":"greek","diet":"vegetarian","intolerances":"gluten","equipment":"pan","includeIngredients":"tomato,cheese","excludeIngredients":"eggs","type":"main course","instructionsRequired":"true","fillIngredients":"false","addRecipeInformation":"false","titleMatch":"Crock Pot","maxReadyTime":"20","ignorePantry":"true","sort":"calories","sortDirection":"asc","minCarbs":"10","maxCarbs":"100","minProtein":"10","maxProtein":"100","minCalories":"50","maxCalories":"800","minFat":"10","maxFat":"100","minAlcohol":"0","maxAlcohol":"100","minCaffeine":"0","maxCaffeine":"100","minCopper":"0","maxCopper":"100","minCalcium":"0","maxCalcium":"100","minCholine":"0","maxCholine":"100","minCholesterol":"0","maxCholesterol":"100","minFluoride":"0","maxFluoride":"100","minSaturatedFat":"0","maxSaturatedFat":"100","minVitaminA":"0","maxVitaminA":"100","minVitaminC":"0","maxVitaminC":"100","minVitaminD":"0","maxVitaminD":"100","minVitaminE":"0","maxVitaminE":"100","minVitaminK":"0","maxVitaminK":"100","minVitaminB1":"0","maxVitaminB1":"100","minVitaminB2":"0","maxVitaminB2":"100","minVitaminB5":"0","maxVitaminB5":"100","minVitaminB3":"0","maxVitaminB3":"100","minVitaminB6":"0","maxVitaminB6":"100","minVitaminB12":"0","maxVitaminB12":"100","minFiber":"0","maxFiber":"100","minFolate":"0","maxFolate":"100","minFolicAcid":"0","maxFolicAcid":"100","minIodine":"0","maxIodine":"100","minIron":"0","maxIron":"100","minMagnesium":"0","maxMagnesium":"100","minManganese":"0","maxManganese":"100","minPhosphorus":"0","maxPhosphorus":"100","minPotassium":"0","maxPotassium":"100","minSelenium":"0","maxSelenium":"100","minSodium":"0","maxSodium":"100","minSugar":"0","maxSugar":"100","minZinc":"0","maxZinc":"100","offset":"0","number":"10","limitLicense":"false","ranking":"2"}

# headers = {
# 	'Content-Type': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
# import requests,pprint
# result=requests.get("https://api.spoonacular.com/food/ingredients/autocomplete?apiKey=b8cf3af47090431c8648f42c61944428&query=appl")
# pprint.pprint(result.json())
# Python code to demonstrate
# converting string to json
# using json.loads
import json
nutri1="{'nutrients': [{'name': 'Vitamin B12', 'amount': 0.0, 'unit': '\u00b5g', 'percentOfDailyNeeds': 0.0}, {'name': 'Fat', 'amount': 0.16, 'unit': 'g', 'percentOfDailyNeeds': 0.25}, {'name': 'Manganese', 'amount': 0.08, 'unit': 'mg', 'percentOfDailyNeeds': 4.01}, {'name': 'Vitamin B3', 'amount': 0.33, 'unit': 'mg', 'percentOfDailyNeeds': 1.67}, {'name': 'Vitamin B6', 'amount': 0.06, 'unit': 'mg', 'percentOfDailyNeeds': 2.82}, {'name': 'Iron', 'amount': 0.78, 'unit': 'mg', 'percentOfDailyNeeds': 4.32}, {'name': 'Calcium', 'amount': 8.4, 'unit': 'mg', 'percentOfDailyNeeds': 0.84}, {'name': 'Vitamin B5', 'amount': 0.01, 'unit': 'mg', 'percentOfDailyNeeds': 0.14}, {'name': 'Protein', 'amount': 0.76, 'unit': 'g', 'percentOfDailyNeeds': 1.51}, {'name': 'Magnesium', 'amount': 9.0, 'unit': 'mg', 'percentOfDailyNeeds': 2.25}, {'name': 'Selenium', 'amount': 0.18, 'unit': '\u00b5g', 'percentOfDailyNeeds': 0.26}, {'name': 'Vitamin D', 'amount': 0.0, 'unit': '\u00b5g', 'percentOfDailyNeeds': 0.0}, {'name': 'Potassium', 'amount': 247.5, 'unit': 'mg', 'percentOfDailyNeeds': 7.07}, {'name': 'Folate', 'amount': 0.9, 'unit': '\u00b5g', 'percentOfDailyNeeds': 0.22}, {'name': 'Phosphorus', 'amount': 22.5, 'unit': 'mg', 'percentOfDailyNeeds': 2.25}, {'name': 'Copper', 'amount': 0.09,'unit': 'mg', 'percentOfDailyNeeds': 4.53}, {'name': 'Mono Unsaturated Fat', 'amount': 0.01, 'unit': 'g', 'percentOfDailyNeeds': 0.0}, {'name': 'Sodium', 'amount': 8.4, 'unit': 'mg', 'percentOfDailyNeeds': 0.37}, {'name': 'Vitamin A', 'amount': 0.0, 'unit': 'IU', 'percentOfDailyNeeds': 0.0}, {'name': 'Zinc', 'amount': 0.05, 'unit': 'mg', 'percentOfDailyNeeds': 0.36}, {'name': 'Vitamin B2', 'amount': 0.05, 'unit': 'mg', 'percentOfDailyNeeds': 3.21}, {'name': 'Saturated Fat', 'amount': 0.05, 'unit': 'g', 'percentOfDailyNeeds': 0.33}, {'name': 'Carbohydrates', 'amount': 23.54, 'unit': 'g', 'percentOfDailyNeeds': 7.85}, {'name': 'Alcohol', 'amount': 0.0, 'unit': 'g', 'percentOfDailyNeeds': 0.0}, {'name': 'Fiber', 'amount': 2.04, 'unit': 'g', 'percentOfDailyNeeds': 8.16}, {'name': 'Vitamin C','amount': 1.62, 'unit': 'mg', 'percentOfDailyNeeds': 1.96}, {'name': 'Calories', 'amount': 88.8, 'unit': 'kcal', 'percentOfDailyNeeds': 4.44}, {'name': 'Vitamin B1', 'amount': 0.03, 'unit': 'mg', 'percentOfDailyNeeds': 2.24}, {'name': 'Folic Acid', 'amount': 0.0, 'unit': '\u00b5g', 'percentOfDailyNeeds': 0.0}, {'name': 'Net Carbohydrates', 'amount': 21.5, 'unit': 'g', 'percentOfDailyNeeds': 7.82}, {'name': 'Poly Unsaturated Fat', 'amount': 0.05, 'unit': 'g', 'percentOfDailyNeeds': 0.0}, {'name': 'Cholesterol', 'amount': 0.0, 'unit': 'mg', 'percentOfDailyNeeds': 0.0}], 'properties': [{'name': 'Glycemic Index', 'amount': 58.8, 'unit': ''}, {'name': 'Glycemic Load', 'amount': 12.64, 'unit': ''}, {'name': 'Nutrition Score', 'amount': 2.013478260869565, 'unit': '%'}], 'flavonoids': [{'name': 'Cyanidin', 'amount': 0.0, 'unit': ''}, {'name': 'Petunidin', 'amount': 0.0, 'unit': ''}, {'name': 'Delphinidin', 'amount': 0.0, 'unit': ''}, {'name': 'Malvidin', 'amount': 0.0, 'unit': ''}, {'name': 'Pelargonidin', 'amount': 0.0, 'unit': ''}, {'name': 'Peonidin', 'amount': 0.0, 'unit': ''}, {'name': 'Catechin', 'amount': 0.0, 'unit': ''}, {'name': 'Epigallocatechin', 'amount': 0.0, 'unit': ''}, {'name': 'Epicatechin', 'amount': 0.0, 'unit': ''}, {'name': 'Epicatechin 3-gallate', 'amount': 0.0, 'unit': ''}, {'name': 'Epigallocatechin 3-gallate', 'amount': 0.0, 'unit': ''}, {'name': 'Theaflavin', 'amount': 0.0, 'unit': ''}, {'name': 'Thearubigins', 'amount': 0.0, 'unit': ''}, {'name': 'Eriodictyol', 'amount': 0.0, 'unit': ''}, {'name': 'Hesperetin', 'amount': 0.0, 'unit': ''}, {'name': 'Naringenin', 'amount': 0.0, 'unit': ''}, {'name': 'Apigenin', 'amount': 0.0, 'unit': ''}, {'name': 'Luteolin', 'amount': 0.0, 'unit': ''}, {'name': 'Isorhamnetin', 'amount': 0.0, 'unit': ''}, {'name': 'Kaempferol', 'amount': 0.0, 'unit': ''}, {'name': 'Myricetin', 'amount': 0.0, 'unit': ''}, {'name': 'Quercetin', 'amount':0.0, 'unit': ''}, {'name': \"Theaflavin-3,3'-digallate\", 'amount': 0.0, 'unit': ''}, {'name': \"Theaflavin-3'-gallate\", 'amount': 0.0, 'unit': ''}, {'name': 'Theaflavin-3-gallate', 'amount': 0.0, 'unit': ''}, {'name': 'Gallocatechin', 'amount': 0.0, 'unit': ''}], 'caloricBreakdown': {'percentProtein': 3.07, 'percentFat': 1.48, 'percentCarbs': 95.45}, 'weightPerServing': {'amount': 30, 'unit': 'g'}"

# inititialising json object
ini_string = {'nikhil': 1, 'akash' : 5,
			'manjeet' : 10, 'akshat' : 15}

# printing initial json
ini_string = json.dumps(ini_string)
print ("initial 1st dictionary", ini_string)
print ("type of ini_object", type(ini_string))

# converting string to json
final_dictionary = json.loads(nutri1)

# printing final result
print ("final dictionary", str(final_dictionary))
print ("type of final_dictionary", type(final_dictionary))
