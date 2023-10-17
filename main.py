from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/design')
def design():
    return render_template("design.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/event')
def event():
    return render_template("event.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
