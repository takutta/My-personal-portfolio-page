from flask import Flask, render_template, session, url_for, redirect
from flask_assets import Bundle, Environment
from livereload import Server

app = Flask(__name__)




assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")
assets.register("css", css)
css.build()

app.debug = True
@app.route('/')
def base_page():
    return render_template(
		'alku.html'
	)

if __name__ == "__main__":
    #app.run(debug=False, host='0.0.0.0')
    server = Server(app.wsgi_app)
    server.serve()