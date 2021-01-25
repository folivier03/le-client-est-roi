from convert_file import csv_dict_list
import connect_db


connect_db.client
#
dict_countries1 = csv_dict_list('countries1.csv')
# #
db = connect_db.client.get_database('country_db')
records = db.country_collection
# # # data insert
records.insert_many(dict_countries1)

#


