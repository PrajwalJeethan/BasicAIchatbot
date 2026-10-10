import os

from flask import Flask, jsonify, render_template, request

from main import match_response

app = Flask(__name__)


@app.after_request
def allow_pages_origin(response):
    allowed_origin = os.environ.get("TOM_ALLOWED_ORIGIN")
    if (
        request.path == "/api/chat"
        and allowed_origin
        and request.headers.get("Origin") == allowed_origin
    ):
        response.headers["Access-Control-Allow-Origin"] = allowed_origin
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.vary.add("Origin")
    return response


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/api/chat")
def chat():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message", "")
    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Write a message before sending."}), 400

    if message.strip().casefold() == "bye":
        return jsonify({"reply": "Good bye, have a great day!", "ended": True})

    return jsonify({"reply": match_response(message), "ended": False})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
