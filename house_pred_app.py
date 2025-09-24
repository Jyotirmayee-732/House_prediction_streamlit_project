from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load("lr_house_model.joblib")

@app.route("/")
def home():
    return render_template("indexH.html")  # Serve the HTML UI

@app.route("/prediction")
def prediction():
    try:
        MedInc = request.args.get("MedInc", type=float)
        HouseAge = request.args.get("HouseAge", type=float)
        Population = request.args.get("Population", type=float)
        AveOccup = request.args.get("AveOccup", type=float)
        Latitude = request.args.get("Latitude", type=float)
        AveRooms = request.args.get("AveRooms", type=float)

        if None in [MedInc, HouseAge, Population, AveOccup, Latitude, AveRooms]:
            return jsonify({"error": "Missing one or more input parameters"}), 400

        input_data = [[MedInc, HouseAge, Population, AveOccup, Latitude, AveRooms]]
        prediction = model.predict(input_data)

        return jsonify({"Prediction": float(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
