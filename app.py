from flask import Flask, render_template, session, url_for, redirect
from livereload import Server
import os

from etusivu import etusivu_bp
from projektit import projektit_bp
from musiikki import musiikki_bp

app = Flask(__name__, static_folder='static')

# Register Blueprintss
app.register_blueprint(etusivu_bp)
app.register_blueprint(projektit_bp)
app.register_blueprint(musiikki_bp)
        
if __name__ == "__main__":
    if os.environ.get("FLASK_ENV") == "production":
        app.run(debug=False, host='0.0.0.0', port=8080)
    else:
        app.debug = True
        server = Server(app.wsgi_app)
        server.serve()
        