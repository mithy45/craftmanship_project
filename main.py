from flask import Flask, request, jsonify

app = Flask(__name__)
links = {}


@app.route("/")
def index():
    return "Hello World"

@app.route("/api/words", methods=["PUT", "GET"])
def api_words_put():
    response = ""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify("Parse Error Json"), 406 
    if not data.get("word"):
        return jsonify("Missing attribut word"), 406 
    if not data.get("translations") or not data["translations"]:
        return jsonify("Missing attribut translations"), 406
    
    for element in data["translations"]:
        if not element.get("language") or not element.get("translation"):
            return jsonify("Missing attribut language or translation in translations"), 406

    links[data["word"]] = data["translations"]
    data["url"] = "http://localhost:8080/api/words/" + data["word"]
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(host="locahost", port=8080)