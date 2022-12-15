from flask import Flask, render_template, session, url_for, redirect
from flask_assets import Bundle, Environment
from livereload import Server

# Import parts of our application
from etusivu import etusivu_bp
from projektit import projektit_bp
from musiikki import musiikki_bp




app = Flask(__name__)

# Register Blueprints
app.register_blueprint(etusivu_bp)
app.register_blueprint(projektit_bp)
app.register_blueprint(musiikki_bp)
        
assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")
assets.register("css", css)
css.build()

app.debug = True

if __name__ == "__main__":
    #app.run(debug=False, host='0.0.0.0')
    server = Server(app.wsgi_app)
    server.serve()