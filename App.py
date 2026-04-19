from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/checkname", methods=["GET", "POST"])
def checkname():
    if request.method == "POST":
        name = request.form["name"]

        if len(name) >= 3:
            msg = "Ism to‘g‘ri"
        else:
            msg = "Ism kamida 3 harf bo‘lishi kerak"

        return render_template("result15.html", msg=msg)

    return render_template("index15.html")

if __name__ == "__main__":
    app.run(debug=True)
