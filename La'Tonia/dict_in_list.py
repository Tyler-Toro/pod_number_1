forty_four = [{'un': 'unstoppable', 'pw': 'unst0pp4bl3!'}, 
{'first_name': 'Hot Spark', 'last_name': 'Sparky Dawn', 'nickname': 'Ghost'}, 
{'initiation_date': '02/13/2027', 'average_days_active': '13', 'last_login_date': '03/23/2033'}, {'fav_online_pastime': 'gaming', 'fav_offline_pastime': 'sleeping', 'fav_lifetime_pastime': 'exploring'}, {'first_comment_tracked': 'You say what now?', 'last_comment_tracked': 'Couldn\'t be'}]

print(forty_four)
print()

# Add to the dictionary nested in a list
forty_four.append({'quirky_dance': 'hop scotch redazzle', 'quirky_mane': 'full width'})
print(forty_four)
print()

# Update dictoionary nested in list ... specifically, initiation date to year 2021
forty_four[2]['initiation_date'] = '02/13/2021'
print(forty_four)

# Update dictoionary nested in list ... specifically, very last item of all content in main dictionary
# This changed the content of what I thought was the last overall item but results for the append I did return last ... interesting
forty_four[4]['last_comment_tracked'] = 'Nah, it can be!'
print(forty_four)
print()
