from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model/xgboost_model.pkl")  # path to your saved model

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict", methods=["POST"])
def predict():
    form = request.form

    input_data = {
        'living area': float(form['living_area']),
        'grade of the house': int(form['grade']),
        'Lattitude': float(form['latitude']),
        'Longitude': float(form['longitude']),
        'living_area_renov': float(form['living_area_renov']),
        'Area of the house(excluding basement)': float(form['area_no_basement']),
        'waterfront present': int(form['waterfront']),
        'Built Year': int(form['built_year']),
        'Postal Code': int(form['postal_code']),
        'number of views': int(form['views']),
    }

    input_df = pd.DataFrame([input_data])
    predicted_price = model.predict(input_df)[0]
    return f"<h2>💰 Predicted Price: ₹{predicted_price:,.2f}</h2><br><a href='/'>← Go Back</a>"




if __name__ == "__main__":
    app.run(debug=True)

# FOR GITHUB
# if __name__ == "__main__":
#     app.run()

