from convert_file import csv_dict_list
import connect_db
import random

connect_db.client
#
# dict_countries1 = csv_dict_list('countries1.csv')
# #
db = connect_db.client.get_database('country_db')
records = db.country_collection
# # data insert
# records.insert_many(dict_countries1)

#
population = random.random()*33097732 
yearly_Change = random.random()*3
net_Change = random.random()*346087
density = random.random()*475.770
land_Area = random.random()*553591
migrants = random.random()*5000
fert_Rate = random.random()*4
med_Age = random.random()*29
urban_Pop = random.random()*59
world_Share = random.random()*16

new_country = {'Country': 'Dubai', 'Population': population, 'Yearly_Change': yearly_Change, ' Net_Change':  net_Change,
                    'Density': density, 'Land_Area': land_Area, 'Migrants': migrants, 'Fert_Rate': fert_Rate, 'Med_Age': med_Age,
                    'Urban_Pop': urban_Pop, 'World_Share': world_Share }

records.insert_one(new_country)