from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/design')
def design():
    return render_template("design.html")

@app.route('/event')
def event():
    return render_template("event.html")

if __name__ == "__main__":
	app.run()

