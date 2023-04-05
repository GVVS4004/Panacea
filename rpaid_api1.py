import requests,os,pprint
import spoonacular as sp
api = sp.API("b8cf3af47090431c8648f42c61944428")
response = api.parse_ingredients("mango")
data = response.json()
pprint.pprint(data)
quant=data[0]['amount']
srcunit=data[0]['unit']
nutrition=data[0]['nutrition']['nutrients']
image=data[0]['image']
# image_url='https://spoonacular.com/cdn/ingredients_100x100/'+str(image)
convert_url='https://api.spoonacular.com/recipes/convert?apiKey=b8cf3af47090431c8648f42c61944428&ingredientName=mango&sourceAmount='+str(quant)+'&sourceUnit='+srcunit+'&targetUnit=grams'
spoonacular_api_convert_url=requests.get(convert_url)
amt=spoonacular_api_convert_url.json()
amount=amt['targetAmount']
autocomplete_url='https://api.spoonacular.com/food/ingredients/autocomplete?apiKey=b8cf3af47090431c8648f42c61944428&query={entry}'

print(amount)

