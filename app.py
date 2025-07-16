from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog")
def bloglar():
    return render_template("bloglar.html")

# Diğer sayfalar
@app.route("/aladaglar")
def aladaglar():
    return render_template("aladaglar.html")

@app.route("/bodrum")
def bodrum():
    return render_template("bodrum.html")

@app.route("/belcika")
def belcika():
    return render_template("belcika.html")

@app.route("/erciyes")
def erciyes():
    return render_template("erciyes.html")

@app.route("/fransa")
def fransa():
    return render_template("fransa.html")

@app.route("/hollanda")
def hollanda():
    return render_template("hollanda.html")

@app.route("/ispanya")
def ispanya():
    return render_template("ispanya.html")

@app.route("/italya")
def italya():
    return render_template("italya.html")

@app.route("/kackarlar")
def kackarlar():
    return render_template("kackarlar.html")

@app.route("/vercenik")
def vercenik():
    return render_template("vercenik.html")

@app.route("/hakkinda")
def hakkinda():
    return render_template("hakkinda.html")

@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")

if __name__ == "__main__":
    app.run(debug=True)
