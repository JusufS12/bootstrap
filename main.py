from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import json, os

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    text = 'ovo je početna stranica!'
    return render_template('index.html',text=text)

@app.route('/columns_equal_3')
def columns_equal_3():  
    return render_template('columns_equal_3.html')

@app.route('/columns_unequal_2')
def columns_unequal_2():  
    return render_template('columns_unequal_2.html')

@app.route('/columns_unequal_3')
def columns_unequal_3():  
    return render_template('columns_unequal_3.html')


def json_extract(path):
    if os.path.exists(path):
        with open(path, mode='r', encoding='utf-8') as json_datoteka:
            data = json.load(json_datoteka)
            json_datoteka.close()
    else:
        data = []
    
    return data

def json_append(data, path):
    data_existing = json_extract('data.json')

    with open(path, mode='w', encoding='utf-8') as json_datoteka:
            data_existing.append(data)
            json.dump(data_existing, json_datoteka)
            json_datoteka.close()



@app.route("/forma", methods=['get', 'post'])
def forma():

    prog_jezici = ['C++', 'Java', 'JavaScript', 'Python', 'Fortran', 'Basic', 'Ruby', 'Rust']

    data = json_extract('data.json')

    if request.method == 'POST':
        ucenik = request.form['ucenik']
        jezik = request.form['programski_jezik']

        redni_broj = len(data) + 1

        json_append({"redni_broj": redni_broj, "ucenik": ucenik, "programski_jezik": jezik}, 'data.json')
        
        return render_template('form.html', redni_broj=1, prog_jezici=prog_jezici, uspjeh=1)
    
    return render_template('form.html', redni_broj=1, prog_jezici=prog_jezici, uspjeh=0)

# Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404