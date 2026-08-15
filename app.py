
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
VERIFY_TOKEN = "123456"  # tem que ser igual ao do Facebook

@app.route("/", methods=["GET"])
def home():
    return "Bot India WhatsApp rodando!"

@app.route("/webhook", methods=["GET"])  # ESSA LINHA NOVA
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == VERIFY_TOKEN:
        return challenge
    return "Token inválido", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Recebi:", data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
