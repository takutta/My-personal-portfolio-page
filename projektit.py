import os
from flask import Blueprint, render_template
from flask import current_app as app
from flask import abort, json

# Blueprint Configuration
projektit_bp = Blueprint(
    'projektit', __name__, template_folder='projektit', static_folder='static'
)

filename = os.path.join(projektit_bp.static_folder, 'projektit.json')
with open(filename, 'r', encoding='utf-8') as projektit:
    projektilista = json.load(projektit)

# Sorttaus järjestyksen mukaan
projektilista = sorted(projektilista, key=lambda x: x['järjestys']) 

@projektit_bp.route('/projektit', methods=['GET'])
def index():
    return render_template(
        'projektit.html', selected = "Projektit", projektilista = projektilista
    )

@projektit_bp.route('/projektit/<name>', methods=['GET'])
def show(name):
#try:
    ' etsitään oikea dict konenimen perusteella'
    for i in range(0, len(projektilista)):
        if projektilista[i]['konenimi'] == name:
            nimi = projektilista[i]['nimi']    
            numero = i
    return render_template('base_projektit.html', projekti = projektilista[numero], projekti_nimi = nimi, selected = "Projektit")
#except:
    abort(404)
    
