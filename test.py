from flask import Flask, jsonify, request

app = Flask(__name__)

# Route pour récupérer un message
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Bonjour !"})

# Route pour envoyer des données
@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"recu": data})

if __name__ == "__main__":
    app.run(debug=True)
