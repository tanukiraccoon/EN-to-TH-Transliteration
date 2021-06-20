from flask import Flask, render_template, request, jsonify
from ml_spellio import use_model  # import การเรียกใช้ model
from back_alignment import reverseChar  # import ตัวตัดคำภาษาอังกฤษ

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    if name:
        words = name.lower()
        result = use_model(words)
        result = reverseChar(result)
        if words.find(",") > -1:
            words = words.replace(",", "")
        #         newName = words + " " + result
        newName = result
        return jsonify({"name": newName, "searchDict": words})
    return jsonify({"error": "Missing data!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
