from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot India WhatsApp rodando!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Recebi:", data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
