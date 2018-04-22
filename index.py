import webScanner
from flask import Flask, render_template
import gc

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    try:
        URL = "https://www.pexels.com"
        s = webScanner.Scanner(URL)
    except:
        return render_template("index.html", dataFound="The web Scanner is sleeping, come back later.", pageTitle="Home page")
    gc.collect()
    pageTitle = s.getPageTitle()
    images = s.getSpecificData()
    return render_template("index.html", pageTitle=pageTitle, images=images)

@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

@app.route("/search/<word>", methods=['GET','POST'])
def search(word=None):
    try:
        URL = "https://www.pexels.com"
        s = webScanner.Scanner(URL + "/search/" + word)
    except:
        return render_template("index.html", dataFound="The web Scanner is sleeping, come back later.", pageTitle="Home page")
    gc.collect()
    pageTitle = s.getPageTitle()
    images = s.getSpecificData()
    return render_template("index.html", pageTitle=pageTitle, images=images)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
