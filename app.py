from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recomendations")
@app.route("/recomendations/<string:man>")
def recomendations(man=""):
    return render_template("recomendations.html", man=man)

@app.route("/all_drugs")
def all_drugs():
    drugs_list = [
        'Парацетамол',
        'Линкас',
        'Антигриппин',
        'Кавинтон',
        'Канефирон'
    ]
    return render_template("all_drugs.html", drugs_list=drugs_list)

    
  