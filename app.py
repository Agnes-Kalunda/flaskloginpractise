from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "AgnesPractise"
    return render_template("index.html",title=title)

@app.route('/about')
def about():
    title = "About Agnes!"
    names = ["Agnes","Neema","Mike","David"]
    return render_template("about.html",names=names, title=title)