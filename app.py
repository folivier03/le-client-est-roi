from flask import Flask
import connect_db
import random

db = connect_db.client.get_database('country_db')
records = db.country_collection
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/find_country/<name_country>')
def get_country(name_country):
    country = records.find_one({'Country': name_country})
    del country['_id']
    return country


@app.route('/api/insert_country/<name_country>')
def add_country(name_country):
      
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

    new_country = {'Country': name_country, 'Population': population, 'Yearly_Change': yearly_Change, ' Net_Change':  net_Change,
                    'Density': density, 'Land_Area': land_Area, 'Migrants': migrants, 'Fert_Rate': fert_Rate, 'Med_Age': med_Age,
                    'Urban_Pop': urban_Pop, 'World_Share': world_Share }

     
    records.insert_one(new_country)
    return "the new country :"+ name_country +"has been added"



@app.route('/api/get_country_tranche/<name_country>')
def get_country_tranche(name_country):
    country = records.find_one({'Country': name_country})
    print(country)
    density = int(country['Density '])

    if  density > 0 and density <300:
        return "Tranche 1"
    elif density > 300 and density <500:
        return "Tranche 2" 

    elif density > 500 and density <1000:
        return "Tranche 3" 
    
    else:
        return "Tranche 4" 






if __name__ == '__main__':
    app.run(host='LOCALHOST', port=8080, debug=True)