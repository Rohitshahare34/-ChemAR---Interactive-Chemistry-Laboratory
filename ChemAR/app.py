from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/experiment/<int:pid>")
def experiment(pid: int):
    if pid not in {1, 2, 3, 4, 5, 6, 7, 8}:
        return render_template("404.html"), 404
    return render_template(f"practical{pid}.html")


@app.route("/lab", methods=["GET", "POST"])
def lab():
    result = None
    if request.method == "POST":
        a = (request.form.get("reactant_a") or "").strip()
        b = (request.form.get("reactant_b") or "").strip()
        cond = (request.form.get("conditions") or "").strip().lower()
        products = []
        notes = ""

        key = f"{a}+{b}".replace(" ", "").lower()
        if key in {"fe+cuso4", "cuso4+fe"}:
            products = ["FeSO4", "Cu"]
            notes = "Single replacement: iron displaces copper from copper sulfate."
        elif key in {"2mg+o2", "mg+o2", "o2+mg"}:
            products = ["MgO"]
            notes = "Synthesis: magnesium oxide forms with bright light."
        elif ("h2o2" in key and ("ki" in key or "catalyst" in cond)):
            products = ["H2O", "O2"]
            notes = "Decomposition catalyzed by KI: oxygen gas and water formed."
        elif ("pb(no3)2" in key and "ki" in key) or ("ki" in key and "pb(no3)2" in key):
            products = ["PbI2", "KNO3"]
            notes = "Precipitation: yellow lead(II) iodide solid forms."
        elif ("na" in key and "cl2" in key):
            products = ["NaCl"]
            notes = "Synthesis: sodium chloride forms."
        else:
            notes = "No rule matched. Showing a generic structure."

        result = {"products": products, "notes": notes}

    return render_template("lab.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)


