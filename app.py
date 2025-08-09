from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status_data():
    return jsonify(
        {
            "status":"todo esta mal"
        }
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)