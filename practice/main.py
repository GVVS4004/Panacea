from website import crete_app
app=crete_app.create_app()

if __name__=='__main__':
    app.run(debug=True)



#  try:
#                 years=db.db.nutrition_info.find_one({'uid':uid})['years']
#                 years[str(cur_year)][str(cur_month)]=cur_month_nutri_info
#                 db.db.nutrition_info.update_one({'uid':uid},{"$set":{'years':years}})
#             except:
#                 db.db.nutrition_info.update_one({'uid':uid},{"$set":{str(cur_year):{(cur_month):cur_month_nutri_info}}})
#         else:
#             # cur_month=cur_month_nutri_info
#             db.db.nutrition_info.insert_one({'uid':uid,"years":{cur_year:{(cur_month):cur_month_nutri_info}}})