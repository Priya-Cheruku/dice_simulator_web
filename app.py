from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    dice_result = None
    if request.method == "POST":
        sides = int(request.form.get("sides", 6))
        dice_result = random.randint(1, sides)
    return render_template("index.html", result=dice_result)

if __name__ == "__main__":
    app.run(debug=True)
