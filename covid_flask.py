from flask import Flask, render_template, request
import datetime
import requests
import json
from covid_io import BrasilIO

app = Flask(__name__)


@app.route("/templates/index.html")
def index():
    return render_template("index.html" ,methods=["GET","POST"])


@app.route("/form", methods=["POST", "GET"])
def form():
    user_agent = "seu-usuario"
    auth_token = "a835b732c90861eb8344542df051729da01deb05"
    api = BrasilIO(user_agent, auth_token)
    dataset_slug = "covid19"
    table_name = "caso_full"

            # Busca por cidade

    cidade_pesq = request.form["cidade"].title()
    data_pesq =request.form['data']
      
    filters = {"search": "{}".format(cidade_pesq.replace(" ","+")), "date": "{}".format(data_pesq)}
    data = api.data(dataset_slug,table_name,filters)
    for row in data:
        cidade = row['city']
        data = row['date']
        populacao = row['estimated_population']
        total_confirm = row['last_available_confirmed']
        mortes = row['last_available_deaths']
        novas_mortes = row['new_deaths']
        novo_confirm = row['new_confirmed']
        
    return render_template("index.html",
                            cidade_pesq = request.form['cidade'].capitalize(),cidade = cidade,
                            data = data,
                            populacao = populacao,
                            total_confirm = total_confirm,
                            mortes = mortes,
                            novas_mortes = novas_mortes,
                            novo_confirm = novo_confirm,
                                      )   

@app.route("/templates/sobre.html")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)                            