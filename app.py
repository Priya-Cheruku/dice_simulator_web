from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    dice_number = None
    if request.method == "POST":
        dice_number = random.randint(1, 6)
    return render_template("index.html", dice_number=dice_number)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

