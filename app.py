
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'gizli_anahtar'  # flash mesajları için

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


# İletişim formu hem GET hem POST destekler, contact.html şablonunu kullanır
@app.route("/iletisim", methods=["GET", "POST"])
def iletisim():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"Gelen iletişim formu:\nAd: {name}\nE-posta: {email}\nMesaj: {message}")
        flash("Mesajınız başarıyla gönderildi! Teşekkür ederiz ❤️")
        return redirect(url_for('iletisim'))
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


