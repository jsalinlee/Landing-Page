from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", name="Floople")
@app.route("/ninjas")
def ninja_page():
    return render_template("ninjas.html")
@app.route("/dojos/new")
def dojos_page():
    return render_template("dojos.html")
app.run(debug=True)
