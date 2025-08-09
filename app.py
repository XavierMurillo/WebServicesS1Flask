from flask import Flask, request, jsonify, render_template

# Se crea una aplicación flask
app = Flask(__name__)

# Se generan rutas según la necesidad del proyecto
@app.route("/status", methods=["GET"])
def status_data():
    return jsonify(
        {
            "status":"todo esta mal"
        }
    )

pulsaciones_globales = 0
@app.route("/pressing", methods=["GET","POST"])
def show_pressing():
    global pulsaciones_globales
    if request.method == "POST":
        pulsaciones_globales = request.get_json().get('pulsaciones')
        return render_template("mostrar_pulsaciones.html", pulsaciones= pulsaciones_globales)
    else:
        return render_template("mostrar_pulsaciones.html", pulsaciones= pulsaciones_globales)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)