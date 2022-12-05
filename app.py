from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/Volbull")
def Volbull():
    return render_template("Volbull.html")

@app.route("/Volbear")
def Volbear():
    return render_template("Volbear.html")


if __name__ == "__main__":
    app.run()
