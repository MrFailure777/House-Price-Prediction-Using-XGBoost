# 🏠 House Price Prediction Using XGBoost

A web-based application to predict house prices using the powerful **XGBoost Regression model**. The model is trained on key housing features such as living area, location, view, year built, and more — to provide accurate predictions of home prices.

![XGBoost](https://img.shields.io/badge/ML-XGBoost-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Backend-Flask-orange?style=flat-square)
![Deployment](https://img.shields.io/badge/Deploy-Render-green?style=flat-square)

---

## 📌 Features

- Predict house prices in real-time using a trained XGBoost model.
- Interactive and responsive web interface using HTML/CSS and JavaScript.
- Popup-based prediction output with close button.
- Navbar with **About** and **Portfolio** links.
- Jupyter Notebooks included for training, visualization, and feature importance.

---

## 🚀 How to Run Locally

### 🔧 1. Clone the Repository
```bash
git clone https://github.com/yourusername/House-Price-Prediction-Using-XGBoost.git
cd House-Price-Prediction-Using-XGBoost
📦 2. Install Requirements

pip install -r requirements.txt
🧠 3. Train (Optional)
Check out the notebooks in the Jupyter Code/ folder to see how the model is trained and saved.

🏃 4. Run the App

python app.py
Then open http://127.0.0.1:5000 in your browser.

📁 Project Structure

House-Price-Prediction-Using-XGBoost/
│
├── model/
│   └── xgboost_model.pkl        # Pre-trained model file
│
├── static/
│   └── style.css                # CSS styles
│
├── templates/
│   ├── index.html               # Main UI
│   └── about.html               # About section
│
├── Jupyter Code/
│   ├── House_Price.ipynb        # Full EDA + model training
│   └── top_10_features.ipynb    # Feature selection notebook
│
├── app.py                       # Flask backend app
├── requirements.txt             # Python dependencies
└── README.md                    # You're reading it!
🔍 Sample Input Fields
Living Area

Grade of the House

Latitude & Longitude

Renovated Area

Area without basement

Waterfront (Yes/No)

Built Year

Postal Code

Number of Views

🌐 Deployment (Render)
You can deploy this app on Render for free.

Connect your GitHub repository

Set:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Deploy and enjoy!

📊 Jupyter Notebooks
Inside the Jupyter Code/ folder, you’ll find:

📘 House_Price.ipynb: Full EDA, visualization, model training.

⭐ top_10_features.ipynb: Feature importance analysis and selection.

📩 Contact
For any queries, reach out to me via:

GitHub: @MrFailure777

Email: jahirulislamofficial5353@gmaill.com

📜 License
This project is open-source under the MIT License.

“Prediction is very difficult, especially if it's about the future.” — Niels Bohr

---

Would you like me to save this as `README.md` and prepare a downloadable version for you?
