from flask import Blueprint, render_template
from flask import current_app as app
from flask import abort

# Blueprint Configuration
projektit_bp = Blueprint(
    'projektit', __name__, template_folder='projektit'
)

projektilista = [{"Nimi":"Hoitoajat Excel", "Järjestys":"10", "Kuva":"", "Esittely":"PäläPälä", "Teknologiat":["Excel","VBA"], "Url":"hoitoajat_excel"},
            {"Nimi":"Lapsisoitin", "Järjestys":"50", "Kuva":"", "Esittely":"Ohjelma näyttää valitsemasi lastenohjelmat Yle Areenalta, TV7:lta jne. jonka jälkeen sammuttaa koneen unitilaan.", "Teknologiat":["Autohotkey"], "Url":"lapsisoitin"},
            {"Nimi":"Kertolaskut", "Järjestys":"30", "Kuva":"", "Esittely":"Peli kertolaskujen oppimiseen", "Teknologiat":["Flask","Bootstrap"], "Url":"kertolaskut"},
            {"Nimi":"Bingo", "Järjestys":"40", "Kuva":"", "Esittely":"Bingo-lappujen generointi ja tulostus", "Teknologiat":["Flask","PaperCSS"], "Url":"bingo"},
            {"Nimi":"Ruokalistat", "Järjestys":"20", "Kuva":"", "Esittely":"Jyväskylän kaupungin päiväkodetien ruokalistojen haku ja tulostus", "Teknologiat":["Flask","Bootstrap"], "Url":"ruokalistat"}
]

# Sorttaus järjestyksen mukaan
projektilista = sorted(projektilista, key=lambda d: d['Järjestys']) 

#tekno-varit = {"Excel":"Blue", "VBA":"Green"}

@projektit_bp.route('/projektit', methods=['GET'])
def index():
    return render_template(
        'projektit.html', selected = "Projektit", projektilista = projektilista
    )

@projektit_bp.route('/projektit/<name>', methods=['GET'])
def show(name):
    try:
        return render_template('%s.html' % name, selected = "Projektit", projektilista = projektilista)
    except:
        abort(404)
    
