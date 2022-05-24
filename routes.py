from flask import render_template, flash, request, url_for
from main import app
from api_connect import BrasilIO

@app.route('/')
def home():
    return render_template('index.html', title= 'Home')

@app.route('/pesquisa', methods=['GET','POST'])
def pesquisa():

    user_agent = "seu-usuario"
    auth_token = "a835b732c90861eb8344542df051729da01deb05"
    api = BrasilIO(user_agent, auth_token)
    dataset = "covid19"
    table_name = "caso_full"
    cidade_pesq = request.form["cidade"].title()
    data_pesq = request.form['data'] 

    filters = {"search": "{}".format(cidade_pesq.replace(
        " ", "+")), "date": "{}".format(data_pesq)}
    data = api.data(dataset, table_name, filters)
    for row in data:
        cidade = row['city']
        estado = row['state']
        data = row['date']
        populacao = row['estimated_population']
        total_confirm = row['last_available_confirmed']
        mortes = row['last_available_deaths']
        novas_mortes = row['new_deaths']
        novo_confirm = row['new_confirmed']
    return render_template("index.html",
                          cidade= f"{cidade} - {estado}",
                           data=data,
                           populacao= f"{populacao} Habitantes",
                           total_confirm=total_confirm,
                           mortes=mortes,
                           novas_mortes=novas_mortes,
                           novo_confirm=novo_confirm, 
                           )

@app.route('/informacoes')
def informacoes():
    return render_template('sobre.html', title='Informacões')