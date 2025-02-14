from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from handleJson import HandleJson


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


@app.route("/forma", methods=['get', 'post'])
def forma():

    prog_jezici = ['C++', 'Java', 'JavaScript', 'Python', 'Fortran', 'Basic', 'Ruby', 'Rust']
    
    data = HandleJson('data.json')
    
    redni_broj = len(data.data) + 1

    if request.method == 'POST':
        ucenik = request.form['ucenik']
        jezik = request.form['programski_jezik']

        data.append({"redni_broj": redni_broj, "ucenik": ucenik, "programski_jezik": jezik})
        
        redni_broj += 1
        
        return redirect(url_for('forma'))
    
    return render_template('form.html', redni_broj=redni_broj, prog_jezici=prog_jezici)


# Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404